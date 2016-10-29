--WPA base

Name: Wi-Fi Protected Access

Description: Wi-Fi Protected Access (WPA) and Wi-Fi Protected Access II (WPA2) are two security protocols and security certification programs developed by the Wi-Fi Alliance to secure wireless computer networks.
The Alliance defined these in response to serious weaknesses researchers had found in the previous system - WEB.

Hardware support: WPA has been designed specifically to work with wireless hardware produced prior to the introduction of WPA protocol,[8] which provides inadequate security through WEP. Some of these devices support WPA only after applying firmware upgrades, which are not available for some legacy devices. Wi-Fi devices certified since 2006 support both the WPA and WPA2 security protocols. WPA2 may not work with some older network cards.

Terminology: Different WPA versions and protection mechanisms can be distinguished based on the target end-user (according to the method of authentication key distribution), and the encryption protocol used.

Target users:
	WPA-Personal: Also referred to as WPA-PSK (pre-shared key) mode, this is designed for home and small office networks and doesn't require an authentication server.[9] Each wireless network device encrypts the network traffic using a 256 bit key. This key may be entered either as a string of 64 hexadecimal digits, or as a passphrase of 8 to 63 printable ASCII characters.If ASCII characters are used, the 256 bit key is calculated by applying the PBKDF2 key derivation function to the passphrase, using the SSID as the salt and 4096 iterations of HMAC-SHA1.WPA-Personal mode is available with both WPA and WPA2.
	WPA-Enterprise: Also referred to as WPA-802.1X mode, and sometimes just WPA (as opposed to WPA-PSK), this is designed for enterprise networks and requires a RADIUS authentication server. This requires a more complicated setup, but provides additional security (e.g. protection against dictionary attacks on short passwords). Various kinds of the Extensible Authentication Protocol (EAP) are used for authentication. WPA-Enterprise mode is available with both WPA and WPA2.
