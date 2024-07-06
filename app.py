from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOCATION_FOLDER = 'allocations'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOCATION_FOLDER'] = ALLOCATION_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(ALLOCATION_FOLDER):
    os.makedirs(ALLOCATION_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    group_file = request.files['group_info']
    hostel_file = request.files['hostel_info']
    
    group_path = os.path.join(app.config['UPLOAD_FOLDER'], 'group_info.csv')
    hostel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'hostel_info.csv')
    
    group_file.save(group_path)
    hostel_file.save(hostel_path)
    
    allocations = allocate_rooms(group_path, hostel_path)
    allocation_path = os.path.join(app.config['ALLOCATION_FOLDER'], 'allocated_rooms.csv')
    allocations.to_csv(allocation_path, index=False)
    
    return send_file(allocation_path, as_attachment=True)

def allocate_rooms(group_file, hostel_file):
    groups = pd.read_csv(group_file)
    hostels = pd.read_csv(hostel_file)
    
    allocations = []
    room_allocations = hostels.copy()
    room_allocations['Allocated'] = 0
    
    for _, group in groups.iterrows():
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']
        
        allocated_rooms = room_allocations[(room_allocations['Gender'] == gender) & (room_allocations['Capacity'] - room_allocations['Allocated'] >= members)]
        
        if not allocated_rooms.empty:
            for _, room in allocated_rooms.iterrows():
                if room['Capacity'] - room['Allocated'] >= members:
                    allocations.append({
                        'Group ID': group_id,
                        'Hostel Name': room['Hostel Name'],
                        'Room Number': room['Room Number'],
                        'Members Allocated': members
                    })
                    room_allocations.loc[room.name, 'Allocated'] += members
                    break
            else:
                allocations.append({
                    'Group ID': group_id,
                    'Hostel Name': 'Unallocated',
                    'Room Number': 'N/A',
                    'Members Allocated': members
                })
        else:
            allocations.append({
                'Group ID': group_id,
                'Hostel Name': 'Unallocated',
                'Room Number': 'N/A',
                'Members Allocated': members
            })
    
    return pd.DataFrame(allocations)

if __name__ == '__main__':
    app.run(debug=True)
