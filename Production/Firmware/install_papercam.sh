set -euo pipefail


APT_PACKAGES=(python3-pip python3-pil python3-gpiozero python3-picamera2 git)
PYPI_PACKAGES=(waveshare-epd)
PHOTOS_DIR="/home/pi/photos"
FIRMWARE_PATH="/home/pi/camera_main.py"
SERVICE_PATH="/etc/systemd/system/papercam.service"
LOG_FILE="/var/log/papercam-install.log"


log() { echo -e "\e[32m>> $*\e[0m"; }
err() { echo -e "\e[31m!! $*\e[0m" >&2; }

require_root() {
  if [[ $EUID -ne 0 ]]; then
    err "This script must be run as root. Use sudo."; exit 1
  fi
}

get_config_file() {
  if [[ -f "/boot/firmware/config.txt" ]]; then
    echo "/boot/firmware/config.txt"
  elif [[ -f "/boot/config.txt" ]]; then
    echo "/boot/config.txt"
  else
    err "Could not find boot config file"; exit 1
  fi
}

enable_interface() {
  local iface=$1
  local config_file
  config_file=$(get_config_file)
  
  if command -v raspi-config &>/dev/null; then
    log "Enabling $iface via raspi-config..."
    raspi-config nonint do_${iface} 0 || true
  else
    log "Enabling $iface via config.txt..."
    case $iface in
      spi) 
        if ! grep -q "dtparam=spi=on" "$config_file"; then
          echo "dtparam=spi=on" >> "$config_file"
          log "Added SPI enable to $config_file"
        else
          log "SPI already enabled in $config_file"
        fi;;
      camera) 
        if ! grep -q "camera_auto_detect=1" "$config_file"; then
          echo "camera_auto_detect=1" >> "$config_file"
          log "Added camera enable to $config_file"
        else
          log "Camera already enabled in $config_file"
        fi;;
    esac
  fi
}

install_debs() {
  log "Installing apt dependencies..."
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get install -y "${APT_PACKAGES[@]}"
}

install_pips() {
  log "Installing Python packages via pip..."
  sudo -u pi pip3 install --user --upgrade pip
  sudo -u pi pip3 install --user "${PYPI_PACKAGES[@]}"
}

verify_installation() {
  log "Verifying Python dependencies..."
  if sudo -u pi python3 -c "import picamera2; print('picamera2: OK')" 2>/dev/null; then
    log "picamera2 verified"
  else
    err "picamera2 verification failed"
  fi
  
  if sudo -u pi python3 -c "from waveshare_epd import epd4in2; print('waveshare-epd: OK')" 2>/dev/null; then
    log "waveshare-epd verified"
  else
    err "waveshare-epd verification failed"
  fi
}

install_firmware_and_service() {
  log "Installing firmware and systemd service..."

  if [[ ! -f "$FIRMWARE_PATH" ]]; then
    err "Firmware file $FIRMWARE_PATH not found. Please copy camera_main.py there."
    exit 1
  fi

  cat <<EOF > "$SERVICE_PATH"
[Unit]
Description=Arya PaperCam Firmware
After=network.target multi-user.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/camera_main.py
WorkingDirectory=/home/pi
Restart=on-failure
RestartSec=3
User=pi
Environment=PYTHONUNBUFFERED=1
StandardOutput=journal
StandardError=journal

# Ensure Pi filesystem is ready
ExecStartPre=/bin/sleep 5

[Install]
WantedBy=multi-user.target
EOF

  chmod 644 "$SERVICE_PATH"
  chown pi:pi "$FIRMWARE_PATH"
  systemctl daemon-reload
  systemctl enable papercam.service
  
  if systemctl is-active --quiet papercam.service; then
    log "Restarting existing papercam service..."
    systemctl restart papercam.service
  else
    log "Starting papercam service..."
    systemctl start papercam.service || true
  fi
}

create_dirs() {
  log "Creating photo directory..."
  mkdir -p "$PHOTOS_DIR"
  chown pi:pi "$PHOTOS_DIR"
}

setup_logging() {
  exec > >(tee -a "$LOG_FILE")
  exec 2>&1
  log "Installation started at $(date)"
}

main() {
  require_root
  setup_logging
  install_debs
  install_pips
  verify_installation
  enable_interface spi
  enable_interface camera
  create_dirs
  install_firmware_and_service
  log "Installation complete!"
  log "Service status:"
  systemctl status papercam.service --no-pager || true
  
  read -rp "Reboot now to enable hardware interfaces? [y/N] " ans
  if [[ ${ans,,} == y* ]]; then
    log "Rebooting..."
    reboot
  else
    log "Please reboot manually for interface changes to take effect."
    log "Check service with: sudo systemctl status papercam.service"
  fi
}

main "$@"