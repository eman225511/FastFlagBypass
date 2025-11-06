#!/usr/bin/env python3
"""
Roblox FastFlag Bypass Tool - Python Version
A tool for managing Roblox FastFlags through IxpSettings.json modification.

WARNING: This tool modifies Roblox client settings and could potentially result 
in account penalties including temporary or permanent bans. USE AT YOUR OWN RISK!
"""

import json
import os
import sys
import shutil
import ctypes
import time
from pathlib import Path
from typing import Dict, Any, Optional


class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'


class FastFlagTool:
    def __init__(self):
        self.local_appdata = os.environ.get('LOCALAPPDATA', '')
        self.ixp_settings_path = Path(self.local_appdata) / 'Roblox' / 'ClientSettings' / 'IxpSettings.json'
        self.script_dir = Path(__file__).parent
        self.backup_dir = self.script_dir / 'backup'
        self.backup_file = self.backup_dir / 'IxpSettings_backup.json'
        self.fastflags_file = self.script_dir / 'fastflags.json'
        
    def is_admin(self) -> bool:
        """Check if the script is running with administrator privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def request_admin(self):
        """Request administrator privileges if not already running as admin"""
        if not self.is_admin():
            print(f"\n{Colors.RED}{'='*80}")
            print(f"{Colors.WHITE}                            ADMINISTRATOR REQUIRED")
            print(f"{Colors.RED}{'='*80}{Colors.END}")
            print(f"\n{Colors.YELLOW}This tool requires administrator privileges to modify protected files.")
            print(f"Please run this script as administrator.{Colors.END}")
            print(f"\n{Colors.CYAN}Right-click on the Python file and select 'Run as administrator'")
            print(f"or run from an elevated command prompt.{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to exit...{Colors.END}")
            sys.exit(1)
    
    def show_warning(self):
        """Display warning message and get user acceptance"""
        print(f"\n{Colors.RED}{'='*80}")
        print(f"{Colors.WHITE}                                    WARNING")
        print(f"{Colors.RED}{'='*80}{Colors.END}")
        print(f"\n{Colors.YELLOW}   This tool modifies Roblox client settings and could potentially result")
        print(f"   in account penalties including temporary or permanent bans.")
        print(f"\n   USE AT YOUR OWN RISK!")
        print(f"\n   The developers of this tool are not responsible for any consequences")
        print(f"   that may occur from using this software.")
        print(f"\n   By continuing, you acknowledge that you understand the risks involved.{Colors.END}")
        print(f"\n{Colors.RED}{'='*80}{Colors.END}")
        
        while True:
            choice = input(f"\n{Colors.WHITE}Press 'Y' to accept the risks and continue, or 'N' to exit: {Colors.END}").strip().lower()
            if choice == 'y':
                break
            elif choice == 'n':
                print(f"\n{Colors.CYAN}Exiting...{Colors.END}")
                time.sleep(1)
                sys.exit(0)
            else:
                print(f"{Colors.RED}Please enter 'Y' or 'N'{Colors.END}")
    
    def show_menu(self):
        """Display the main menu"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{Colors.GREEN}{'='*80}")
        print(f"{Colors.WHITE}                            Roblox FastFlag Bypass Tool")
        print(f"                                   Version 2.0 (Python)")
        print(f"{Colors.GREEN}{'='*80}{Colors.END}")
        print(f"\n{Colors.CYAN}{'-'*80}")
        print(f"{Colors.WHITE}                                    OPTIONS")
        print(f"{Colors.CYAN}{'-'*80}{Colors.END}")
        print(f"\n{Colors.WHITE}    [1] Backup IxpSettings.json")
        print(f"    [2] Append FastFlags (and set read-only)")
        print(f"    [3] Apply Fleasion FastFlag (FFlagHttpUseRbxStorage10: false)")
        print(f"    [4] Restore from backup")
        print(f"    [5] Help and Instructions")
        print(f"    [6] Exit{Colors.END}")
        print(f"\n{Colors.CYAN}{'-'*80}{Colors.END}")
    
    def get_choice(self) -> str:
        """Get user menu choice with validation"""
        while True:
            try:
                choice = input(f"\n{Colors.WHITE}   Enter your choice (1-6): {Colors.END}").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print(f"{Colors.RED}Invalid choice. Please enter a number between 1-6.{Colors.END}")
            except KeyboardInterrupt:
                print(f"\n\n{Colors.CYAN}Exiting...{Colors.END}")
                sys.exit(0)
    
    def ensure_backup_dir(self):
        """Ensure backup directory exists"""
        self.backup_dir.mkdir(exist_ok=True)
    
    def backup_settings(self):
        """Create a backup of IxpSettings.json"""
        print(f"\n{Colors.BLUE}{'='*80}")
        print(f"{Colors.WHITE}                                 BACKUP MODE")
        print(f"{Colors.BLUE}{'='*80}{Colors.END}")
        
        if not self.ixp_settings_path.exists():
            print(f"\n{Colors.RED}[ERROR] IxpSettings.json not found at:")
            print(f"    {self.ixp_settings_path}")
            print(f"\n[TIP] Make sure Roblox is installed and has been run at least once.{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
            return
        
        if self.backup_file.exists():
            print(f"\n{Colors.YELLOW}[WARNING] Backup already exists at:")
            print(f"    {self.backup_file}")
            print(f"\n[IMPORTANT] Only overwrite if you're sure the current IxpSettings.json")
            print(f"             contains your ORIGINAL settings (not modified ones).")
            print(f"\n[TIP] If you've already appended FastFlags, this backup may contain")
            print(f"      your modified settings. Consider renaming the existing backup first.{Colors.END}")
            
            while True:
                overwrite = input(f"\n{Colors.WHITE}Do you want to overwrite the existing backup? (y/n): {Colors.END}").strip().lower()
                if overwrite == 'y':
                    break
                elif overwrite == 'n':
                    print(f"\n{Colors.CYAN}Backup cancelled - existing backup preserved.{Colors.END}")
                    input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
                    return
                else:
                    print(f"{Colors.RED}Please enter 'y' or 'n'{Colors.END}")
        
        try:
            self.ensure_backup_dir()
            print(f"\n{Colors.CYAN}[INFO] Creating backup...{Colors.END}")
            shutil.copy2(self.ixp_settings_path, self.backup_file)
            print(f"\n{Colors.GREEN}[SUCCESS] Backup created successfully!")
            print(f"    Location: {self.backup_file}{Colors.END}")
            
        except Exception as e:
            print(f"\n{Colors.RED}[ERROR] Failed to create backup: {str(e)}{Colors.END}")
        
        input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
    
    def load_json_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Load and parse a JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"{Colors.RED}[ERROR] Invalid JSON in {file_path}: {str(e)}{Colors.END}")
            return None
        except Exception as e:
            print(f"{Colors.RED}[ERROR] Failed to read {file_path}: {str(e)}{Colors.END}")
            return None
    
    def save_json_file(self, file_path: Path, data: Dict[str, Any]):
        """Save data to a JSON file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, separators=(',', ':'))
        except Exception as e:
            print(f"{Colors.RED}[ERROR] Failed to save {file_path}: {str(e)}{Colors.END}")
            raise
    
    def set_file_readonly(self, file_path: Path, readonly: bool = True):
        """Set or remove read-only attribute on Windows"""
        try:
            if os.name == 'nt':  # Windows
                import stat
                if readonly:
                    os.chmod(file_path, stat.S_IREAD)
                else:
                    os.chmod(file_path, stat.S_IWRITE | stat.S_IREAD)
        except Exception as e:
            print(f"{Colors.YELLOW}[WARNING] Could not change file attributes: {str(e)}{Colors.END}")
    
    def append_fastflags(self):
        """Append FastFlags from fastflags.json to IxpSettings.json"""
        print(f"\n{Colors.YELLOW}{'='*80}")
        print(f"{Colors.WHITE}                              APPEND FASTFLAGS MODE")
        print(f"{Colors.YELLOW}{'='*80}{Colors.END}")
        
        if not self.fastflags_file.exists():
            print(f"\n{Colors.RED}[ERROR] fastflags.json not found at:")
            print(f"    {self.fastflags_file}{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
            return
        
        if not self.ixp_settings_path.exists():
            print(f"\n{Colors.RED}[ERROR] IxpSettings.json not found at:")
            print(f"    {self.ixp_settings_path}")
            print(f"\n[TIP] Make sure Roblox is installed and has been run at least once.{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
            return
        
        try:
            # Remove read-only attribute temporarily
            self.set_file_readonly(self.ixp_settings_path, False)
            
            print(f"\n{Colors.CYAN}[INFO] Processing files...{Colors.END}")
            
            # Load fastflags
            fastflags = self.load_json_file(self.fastflags_file)
            if fastflags is None:
                input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
                return
            
            # Load existing settings
            existing_settings = self.load_json_file(self.ixp_settings_path)
            if existing_settings is None:
                existing_settings = {}
            
            # Merge fastflags into existing settings
            print(f"\n{Colors.CYAN}[INFO] Merging FastFlags...{Colors.END}")
            existing_settings.update(fastflags)
            
            # Save merged settings
            self.save_json_file(self.ixp_settings_path, existing_settings)
            
            # Set file as read-only
            print(f"\n{Colors.CYAN}[INFO] Setting file as read-only...{Colors.END}")
            self.set_file_readonly(self.ixp_settings_path, True)
            
            print(f"\n{Colors.GREEN}[SUCCESS] FastFlags appended successfully!")
            print(f"[INFO] File set to read-only protection.{Colors.END}")
            
        except Exception as e:
            print(f"\n{Colors.RED}[ERROR] Failed to append FastFlags: {str(e)}{Colors.END}")
        
        input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
    
    def apply_fleasion_flag(self):
        """Apply the Fleasion FastFlag directly"""
        print(f"\n{Colors.MAGENTA}{'='*80}")
        print(f"{Colors.WHITE}                            FLEASION FASTFLAG MODE")
        print(f"{Colors.MAGENTA}{'='*80}{Colors.END}")
        print(f"\n{Colors.CYAN}[INFO] This will apply the Fleasion FastFlag:")
        print(f"       FFlagHttpUseRbxStorage10: false")
        print(f"\n[PURPOSE] Disables HTTP RbxStorage10 - commonly used for performance/compatibility{Colors.END}")
        
        if not self.ixp_settings_path.exists():
            print(f"\n{Colors.RED}[ERROR] IxpSettings.json not found at:")
            print(f"    {self.ixp_settings_path}")
            print(f"\n[TIP] Make sure Roblox is installed and has been run at least once.{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
            return
        
        if not self.backup_file.exists():
            print(f"\n{Colors.YELLOW}[WARNING] No backup found!")
            print(f"\n[IMPORTANT] It's strongly recommended to create a backup first.")
            print(f"             This protects your original settings if something goes wrong.{Colors.END}")
            
            while True:
                continue_choice = input(f"\n{Colors.WHITE}Do you want to continue without a backup? (y/n): {Colors.END}").strip().lower()
                if continue_choice == 'y':
                    break
                elif continue_choice == 'n':
                    print(f"\n{Colors.CYAN}Operation cancelled. Please create a backup first (option 1).{Colors.END}")
                    input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
                    return
                else:
                    print(f"{Colors.RED}Please enter 'y' or 'n'{Colors.END}")
        
        try:
            # Remove read-only attribute temporarily
            self.set_file_readonly(self.ixp_settings_path, False)
            
            print(f"\n{Colors.CYAN}[INFO] Applying Fleasion FastFlag...{Colors.END}")
            
            # Load existing settings
            existing_settings = self.load_json_file(self.ixp_settings_path)
            if existing_settings is None:
                existing_settings = {}
            
            # Add Fleasion flag
            existing_settings["FFlagHttpUseRbxStorage10"] = "false"
            
            # Save settings
            self.save_json_file(self.ixp_settings_path, existing_settings)
            
            # Set file as read-only
            print(f"\n{Colors.CYAN}[INFO] Setting file as read-only...{Colors.END}")
            self.set_file_readonly(self.ixp_settings_path, True)
            
            print(f"\n{Colors.GREEN}[SUCCESS] Fleasion FastFlag applied successfully!")
            print(f"[INFO] FFlagHttpUseRbxStorage10 set to false")
            print(f"[INFO] File set to read-only protection.{Colors.END}")
            
        except Exception as e:
            print(f"\n{Colors.RED}[ERROR] Failed to apply Fleasion FastFlag: {str(e)}{Colors.END}")
        
        input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
    
    def restore_from_backup(self):
        """Restore IxpSettings.json from backup"""
        print(f"\n{Colors.MAGENTA}{'='*80}")
        print(f"{Colors.WHITE}                               RESTORE MODE")
        print(f"{Colors.MAGENTA}{'='*80}{Colors.END}")
        
        if not self.backup_file.exists():
            print(f"\n{Colors.RED}[ERROR] No backup found at:")
            print(f"    {self.backup_file}")
            print(f"\n[TIP] Please create a backup first using option 1.{Colors.END}")
            input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
            return
        
        try:
            # Ensure the directory structure exists
            self.ixp_settings_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Remove read-only attribute if file exists
            if self.ixp_settings_path.exists():
                print(f"\n{Colors.CYAN}[INFO] Removing read-only protection...{Colors.END}")
                self.set_file_readonly(self.ixp_settings_path, False)
            
            print(f"\n{Colors.CYAN}[INFO] Restoring from backup...{Colors.END}")
            shutil.copy2(self.backup_file, self.ixp_settings_path)
            
            print(f"\n{Colors.GREEN}[SUCCESS] File restored successfully from backup!")
            print(f"[INFO] Read-only attribute removed.{Colors.END}")
            
        except Exception as e:
            print(f"\n{Colors.RED}[ERROR] Failed to restore from backup: {str(e)}{Colors.END}")
        
        input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
    
    def show_help(self):
        """Display help and instructions"""
        print(f"\n{Colors.WHITE}{'='*80}")
        print(f"                               HELP AND INSTRUCTIONS")
        print(f"{'='*80}{Colors.END}")
        
        help_text = f"""
{Colors.CYAN}[GETTING STARTED - First Time Setup]{Colors.END}

{Colors.WHITE}  1. First, create a backup of your original settings (IMPORTANT!)
     - Choose option 1 to backup IxpSettings.json
     - This protects your original Roblox settings
     - Only do this ONCE with clean/original settings
     - Don't overwrite backup after appending FastFlags!

  2. Add your FastFlags to the fastflags.json file
     - Open fastflags.json in a text editor
     - Add your flags in proper JSON format:
       {{"FFlagName1":"value1","FFlagName2":"value2"}}
     - Save the file

  3. Apply the FastFlags
     - Choose option 2 to append FastFlags
     - This merges your flags with existing Roblox settings
     - File becomes read-only to prevent Roblox from changing it

  OR use the Quick Fleasion Option:
     - Choose option 3 for instant Fleasion FastFlag application
     - Applies {{"FFlagHttpUseRbxStorage10": "false"}} directly
     - No need to edit fastflags.json manually{Colors.END}

{Colors.CYAN}[CHANGING FASTFLAGS]{Colors.END}

{Colors.WHITE}  To modify your FastFlags:
  1. Choose option 4 to restore from backup (gets original settings)
  2. Edit fastflags.json with your new settings
  3. Choose option 2 to append the updated flags
  4. DO NOT create a new backup at this point!{Colors.END}

{Colors.CYAN}[BACKUP SAFETY]{Colors.END}

{Colors.WHITE}  - Only backup your ORIGINAL/CLEAN Roblox settings
  - Don't backup after you've appended FastFlags
  - The backup should only contain vanilla Roblox settings
  - If you accidentally backup modified settings, you'll lose originals{Colors.END}

{Colors.CYAN}[IMPORTANT TIPS]{Colors.END}

{Colors.WHITE}  - Close Roblox completely before running this tool
  - Test flags one at a time to identify issues
  - Some flags may cause crashes or unexpected behavior
  - Roblox updates may reset your settings{Colors.END}

{Colors.CYAN}[TROUBLESHOOTING]{Colors.END}

{Colors.WHITE}  - If Roblox won't start: Restore from backup (option 4)
  - If flags don't work: Check JSON syntax in fastflags.json
  - If file is locked: Run this tool as administrator
  - If backup fails: Check Roblox is installed and run at least once{Colors.END}

{Colors.CYAN}[JSON FORMAT EXAMPLE]{Colors.END}

{Colors.WHITE}  fastflags.json should look like this:
  {{
    "FFlagDebugForceFutureIsBright": "True",
    "FFlagUserShowGuiHideToggles": "True",
    "DFIntCanHideGuiGroupId": "0"
  }}{Colors.END}

{Colors.RED}[IMPORTANT]{Colors.END}
{Colors.YELLOW}Remember: Use this tool at your own risk!
The developers are not responsible for any consequences.{Colors.END}
"""
        print(help_text)
        input(f"\n{Colors.WHITE}Press Enter to return to menu...{Colors.END}")
    
    def run(self):
        """Main application loop"""
        self.request_admin()
        self.show_warning()
        
        while True:
            self.show_menu()
            choice = self.get_choice()
            
            print(f"\n{Colors.CYAN}{'-'*80}{Colors.END}")
            
            if choice == '1':
                self.backup_settings()
            elif choice == '2':
                self.append_fastflags()
            elif choice == '3':
                self.apply_fleasion_flag()
            elif choice == '4':
                self.restore_from_backup()
            elif choice == '5':
                self.show_help()
            elif choice == '6':
                print(f"\n{Colors.CYAN}Thanks for using Roblox FastFlag Bypass Tool!")
                print(f"Goodbye!{Colors.END}")
                time.sleep(1)
                break


if __name__ == "__main__":
    try:
        tool = FastFlagTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}Operation cancelled by user. Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {str(e)}{Colors.END}")
        input(f"\n{Colors.WHITE}Press Enter to exit...{Colors.END}")