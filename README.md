# Healthcare Management System

This project implements a comprehensive healthcare management system that manages patients, appointments, medical terms, and inventory. It includes various data structures like Linked Lists, Binary Search Trees, Heaps, and Tries to efficiently manage and retrieve information.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Classes and Data Structures](#classes-and-data-structures)
- [Functions and Methods](#functions-and-methods)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Patient Management**: Add, search, and retrieve patient information.
- **Appointment Scheduling**: Schedule, retrieve, and display appointments.
- **Inventory Management**: Manage healthcare inventory.
- **Patient History**: Maintain and retrieve patient history.
- **Medical Terms Management**: Insert, search, and suggest medical terms using Trie.
- **Priority Queue**: Efficient handling of appointment queues.
- **Interactive Menu**: User-friendly CLI for managing the system.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/UniversityOfEmergingTechnology/capstone-project-dsa.git
   ```
2. **Navigate to the project directory**:
   ```sh
   cd healthcare-management-system
   ```
3. **Run the system**:
   ```sh
   python main.py
   ```

## Usage

- The system provides an interactive menu to manage patients, appointments, inventory, and medical terms.
- Follow the on-screen instructions to navigate through the menu and perform various operations.

## Classes and Data Structures

### `LinkedListNode`
- Node class for Linked List.

### `LinkedList`
- Manages patient history using linked list.

### `Patient`
- Stores patient information including ID, name, age, blood type, and history.

### `Appointment`
- Stores appointment information including ID, patient, date, and time.

### `BinarySearchTree`
- Efficient search and management of patient records.

### `PriorityQueue`
- Manages appointment queues.

### `Trie`
- Manages medical terms.

### `HealthCareManagementSystem`
- Main class to manage the overall healthcare system.

## Functions and Methods

- **Patient Management**:
  - `add_patient(name, age, blood_type)`: Adds a new patient.
  - `get_patient_history(patient_id)`: Retrieves patient history.
  - `add_patient_history(patient_id, history_entry)`: Adds an entry to patient history.

- **Appointment Management**:
  - `schedule_appointment(patient_id, date, time)`: Schedules a new appointment.
  - `get_appointment_schedule()`: Retrieves and returns the appointment schedule.
  - `display_ordered_appointments()`: Displays ordered appointments by date and time.

- **Inventory Management**:
  - `manage_inventory(item)`: Adds an item to inventory.

- **Medical Terms Management**:
  - `insert_medicial_term(term)`: Inserts a medical term.
  - `search_medical_term(term)`: Searches for a medical term.
  - `suggest_medical_terms(prefix)`: Suggests medical terms based on a prefix.

- **Interactive Menu**:
  - `display_menu()`: Displays the menu options.
  - `handle_menu()`: Handles the user input for the menu.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
