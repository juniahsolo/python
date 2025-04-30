import os
from datetime import datetime

def get_modified_filename(original_name):
    """Generate a modified filename with timestamp"""
    base, ext = os.path.splitext(original_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base}_modified_{timestamp}{ext}"

def modify_content(content, operation):
    """Apply the specified modification to content"""
    operations = {
        'upper': content.upper(),
        'lower': content.lower(),
        'title': content.title(),
        'reverse': '\n'.join(reversed(content.splitlines())),
        'double': '\n'.join([line*2 for line in content.splitlines()])
    }
    return operations.get(operation, content)

def file_modifier():
    """Main function with enhanced features"""
    print("\n📂 ENHANCED FILE MODIFIER 📂")
    print("1. Enter a filename to read")
    print("2. Choose modification type")
    print("3. Get a timestamped output file")
    print("---------------------------------")
    
    while True:
        try:
            filename = input("\nEnter filename (or 'quit'): ").strip()
            if filename.lower() == 'quit':
                print("👋 Exiting program...")
                return
            
            # Verify file exists before proceeding
            if not os.path.exists(filename):
                raise FileNotFoundError(f"'{filename}' doesn't exist")
                
            # Get modification type
            print("\nAvailable modifications:")
            print("1. Uppercase (upper)")
            print("2. Lowercase (lower)")
            print("3. Title Case (title)")
            print("4. Reverse Lines (reverse)")
            print("5. Double Lines (double)")
            mod_choice = input("Choose modification (1-5 or 'skip'): ").strip().lower()
            
            mod_map = {
                '1': 'upper',
                '2': 'lower',
                '3': 'title',
                '4': 'reverse',
                '5': 'double',
                'skip': None
            }
            operation = mod_map.get(mod_choice, None)
            
            # Process file
            with open(filename, 'r') as original_file:
                content = original_file.read()
                
                if operation:
                    modified_content = modify_content(content, operation)
                    new_filename = get_modified_filename(filename)
                    
                    with open(new_filename, 'w') as new_file:
                        new_file.write(modified_content)
                    
                    print(f"\n✅ Success! Created '{new_filename}'")
                    print(f"📊 Stats: {len(content.splitlines())} lines processed")
                    print(f"📝 Modified using: {operation} operation")
                    
                    # Push to GitHub option
                    if input("\nPush to GitHub? (y/n): ").lower() == 'y':
                        push_to_github(new_filename)
                else:
                    print("\n⚠️ No modifications made")
            
            if input("\nProcess another file? (y/n): ").lower() != 'y':
                break
                
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again\n")

def push_to_github(filename):
    """Helper function to push file to GitHub"""
    try:
        # These commands would need your Git configuration
        commands = [
            'git add {filename}',
            f'git commit -m "Added modified file {filename}"',
            'git push origin main'
        ]
        
        print("\n🔄 Attempting to push to GitHub...")
        for cmd in commands:
            os.system(cmd.format(filename=filename))
        print("✅ Successfully pushed to GitHub!")
        
    except Exception as e:
        print(f"❌ Failed to push to GitHub: {str(e)}")

if __name__ == "__main__":
    file_modifier()