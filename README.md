# Digitalization of the Hospitality Process

This project is a Flask-based web application designed to allocate rooms in hostels based on group and hostel information provided in CSV files.

## Features
- Upload CSV files containing group and hostel information.
- Process the files and allocate rooms.
- Download the allocation results as a CSV file.

## Requirements
- Python 3.x
- Flask
- Pandas

## Installation and Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RoomAllocationApp.git
    cd RoomAllocationApp
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Data Files
Sample data files are included in the `uploads` folder. These files are used for testing the application:

### CSV File 1 (Group Information)
Contains information about groups with a common ID. Each row represents a group, specifying the group ID, the number of members, and the gender (boys or girls). There can be various scenarios under the same registration ID: groups of different sizes such as 2, 3, 4, 5, 6, or 7 people or more; groups consisting only of boys or girls; and groups containing both boys and girls under the same registration ID.

**group_info.csv**
| Group ID | Members | Gender           |
|----------|---------|------------------|
| 101      | 3       | Boys             |
| 102      | 4       | Girls            |
| 103      | 2       | Boys             |
| 104      | 5       | Girls            |
| 105      | 8       | 5 Boys & 3 Girls |

### CSV File 2 (Hostel Information)
Contains information about the hostels and their room capacities. Each row represents a hostel room, specifying the hostel name, room number, room capacity, and gender accommodation (boys or girls).

**hostel_info.csv**
| Hostel Name   | Room Number | Capacity | Gender |
|---------------|-------------|----------|--------|
| Boys Hostel A | 101         | 3        | Boys   |
| Boys Hostel A | 102         | 4        | Boys   |
| Girls Hostel B| 201         | 2        | Girls  |
| Girls Hostel B| 202         | 5        | Girls  |

### Output
A display of the allocated rooms indicating which group members are in which room. A downloadable CSV file with the allocation details is generated after the allocation process.

**allocated_rooms.csv**
| Group ID | Hostel Name    | Room Number | Members Allocated |
|----------|----------------|-------------|-------------------|
| 101      | Boys Hostel A  | 101         | 3                 |
| 102      | Girls Hostel B | 202         | 4                 |
| 103      | Boys Hostel A  | 102         | 2                 |
| 104      | Girls Hostel B | 202         | 5                 |

