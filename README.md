# Telegram Message Forwarder

Python-скрипт для пересилання повідомлень між Telegram-групами.

## Запуск
```bash
pip install -r requirements.txt
python forward_messages.py


/etc/systemd/system/health-msg-resend.service

systemctl daemon-reload
systemctl enable health-msg-resend
systemctl start health-msg-resend


[Unit]
Description=Telegram Health Message Resend
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/root/health_msg_resend
ExecStart=/home/root/health_msg_resend/venv/bin/python forward_messages.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
