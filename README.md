# LED Screen Wire Size Calculator

A simple and effective tool to calculate the appropriate electrical wire size for LED screen installations. This project provides two versions: a user-friendly web interface and a command-line Python script.

The calculator helps determine the correct wire gauge, cable type, and circuit breaker size based on the screen's dimensions, power consumption, and installation environment.

## Features

-   **Power Calculation:** Automatically calculates the total power consumption (in Watts) based on screen area and power density.
-   **Phase Support:** Supports both single-phase (220V) and three-phase (380V) electrical systems.
-   **Installation Types:** Accounts for different installation methods (e.g., in conduit, exposed, or buried) by applying appropriate derating factors and suggesting suitable cable types (THW, VCT, NYY).
-   **Wire Sizing:** Recommends the appropriate wire size (in mm²) based on the calculated current and standard ampacity tables (TIS 11-2553).
-   **Circuit Planning:** Suggests the required number of circuits and a suitable Main Circuit Breaker (MCB) rating for safety.
-   **Dual Interface:** Choose between an interactive web calculator (`index.html`) or a terminal-based Python script (`cable calculator.py`).
-   **Localized:** The user interface and code comments are provided in Thai for ease of use.

## How to Use

### Web Version (`index.html`)

This is the easiest way to use the calculator. No installation is required.

1.  Open the `index.html` file in any modern web browser.
2.  Fill in the input fields:
    *   **Width** and **Height** of the LED screen (in meters).
    *   **Power consumption** (in Watts per square meter).
    *   Select the **Phase** (1 Phase or 3 Phase).
    *   Choose the **Installation Type**.
3.  Click the **"Calculate"** button.
4.  The results, including the recommended cable type, wire size, ampacity, and circuit breaker details, will be displayed below the form.

### Command-Line Version (`cable calculator.py`)

For users who prefer a terminal interface.

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed on your system.
2.  Open your terminal or command prompt.
3.  Navigate to the project directory where the script is located.
4.  Run the script with the following command:
    ```sh
    python "cable calculator.py"
    ```
5.  Follow the on-screen prompts to enter the required values. The results will be printed directly in the terminal.

## Calculation Logic

The calculation process follows standard electrical principles:

1.  **Total Power (Watts):** `Screen Width × Screen Height × Power per m²`
2.  **Total Current (Amps):** Calculated using the power formula, accounting for the system voltage (220V/380V) and a standard power factor (0.95).
3.  **Required Current:** The total current is divided by a derating factor (e.g., 0.8 for wires in conduit) to determine the current capacity the wire must handle.
4.  **Wire Size Selection:** The script looks up the required current in a predefined table of standard wire gauges and their ampacities to find the smallest size that can safely handle the load.
5.  **Circuit Breaker & Count:** A suitable circuit breaker size is determined (typically 80% of the wire's ampacity). If the total current exceeds the breaker's rating, the calculator suggests splitting the load across multiple circuits.

## Technologies Used

-   **HTML5**
-   **Bootstrap 5** for styling the web interface.
-   **JavaScript** for the client-side calculation logic in the web version.
-   **Python 3** for the command-line version.