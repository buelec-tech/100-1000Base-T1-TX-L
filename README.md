# 100/1000Base-T1-TX-L Automotive Ethernet Media Converter

The **BUELEC 100/1000Base-T1-TX-L** is a compact, bidirectional physical layer converter designed for seamless interoperability between standard RJ45 Ethernet (**100/1000Base-TX**) and dual-wire automotive Ethernet (**100/1000Base-T1**). 

Built on field-proven silicon—**Marvell 88Q2112** for the T1 side and **Realtek RTL8211FI** for the TX side—this converter ensures zero packet loss, ultra-low latency, and rock-solid stability for automotive diagnostic, testing, and integration applications.

---

## Key Features

*   **Dual-Speed Support**: Fully compliant with IEEE 802.3bw (100BASE-T1) and IEEE 802.3bp (1000BASE-T1).
*   **Automotive Grade PHY**: Features the AEC-Q100 qualified Marvell 88Q2112 for superior EMI resistance and reliability.
*   **Broad Compatibility**: Interoperable with automotive Ethernet PHYs from NXP, TI, Broadcom, Marvell, and Realtek.
*   **Flexible Power Options**: Dual-input design via 5.5mm DC barrel jack (5–36V) and USB Type-C (5V).
*   **Industrial Durability**: CNC-machined sandblasted aluminum alloy housing with an operating temperature range of -45°C to +85°C.
*   **Real-time Diagnostics**: Integrated LEDs for Link/Activity and a Signal Quality Indicator (SQI) for the 1Gbps mode.
*   **Plug-and-Play**: Driver-free operation across Windows, Linux, and macOS.

---

## Hardware Specifications

| Item | Specification |
| :--- | :--- |
| **T1 PHY Chip** | Marvell 88Q2112 (AEC-Q100) |
| **TX PHY Chip** | Realtek RTL8211FI |
| **Power Input** | USB Type-C (5V/2A) or DC-JACK 5.5*2.1 (5-36V) |
| **Case Material** | Sandblasted Aluminum Alloy |
| **Operating Temp** | -45°C to +85°C |
| **Dimensions** | 103mm x 71mm x 26mm |
| **Weight** | 0.2kg |

---

## Interface & Controls

### Connectors
1.  **Standard Ethernet**: RJ45 port for 100/1000Base-TX.
2.  **Automotive Ethernet**: 2-pin 3.81mm pitch terminal for 100/1000Base-T1.
3.  **Adapters Included**: 
    *   1× TE MATE-NET adapter board (Part: 2304372-1)
    *   1× HMTD adapter board (Part: E6S20A-40MT5-Z)

### Switches
*   **Master/Slave Selection**: One device must be set as Master and the other as Slave to establish a T1 link.
*   **100M/1000M Selection**: Manual toggle for working mode selection.

---

## Quick Start Guide (Linux/Raspberry Pi)

### 1. Install iperf3
```bash
sudo apt-get update
sudo apt-get install iperf3
```

### 2. Network Configuration
Set static IPs for testing (e.g., Host A: `190.19.1.9`, Host B: `190.19.1.90`):
```bash
sudo ifconfig eth0 190.19.1.9 up
```

### 3. Performance Testing
*   **Server Side (Host B)**: `iperf3 -s`
*   **Client Side (Host A)**: `iperf3 -c 190.19.1.90 -t 30`

For automated testing, refer to the Python scripts in the [`Linux_Python/`](./Linux_Python/) directory.

---

## Repository Structure

*   [`Linux_Python/`](./Linux_Python/): Python scripts for IP configuration, ping, and iperf3 testing.
*   [`Win_Soft/`](./Win_Soft/): iperf3 binaries for Windows.
*   [`100-1000BASE-T1TX-L User Manual-V12.pdf`](./100-1000BASE-T1TX-L%20User%20Manual-V12.pdf): Full technical documentation.

---

## Support

*   **Website**: [www.buelec-tech.com](https://www.buelec-tech.com)
*   **Email**: [support@buelec-tech.com](mailto:support@buelec-tech.com) | [sales@buelec-tech.com](mailto:sales@buelec-tech.com)
