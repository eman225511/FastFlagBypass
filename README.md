# Roblox FastFlag Bypass Tool

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/eman225511/FastFlagBypass)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/en-us/windows)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A modern Python tool for safely managing Roblox FastFlags with comprehensive backup and safety features.

## 🚀 Version 2.0 - Python Rewrite

**NEW**: Complete rewrite in Python for improved reliability, better error handling, and enhanced user experience!

### What's New
- ✅ **Rock-solid stability** - No more batch script syntax errors
- ✅ **Native JSON handling** - Proper JSON parsing and validation
- ✅ **Colored terminal interface** - Easy-to-read output with color coding
- ✅ **Enhanced error handling** - Clear error messages and recovery options
- ✅ **Cross-platform foundation** - Ready for future multi-platform support
- ✅ **Improved file operations** - Reliable file handling and permissions

## ⚠️ WARNING

**USE AT YOUR OWN RISK!** This tool modifies Roblox client settings and could potentially result in account penalties including temporary or permanent bans. The developers of this tool are not responsible for any consequences that may occur from using this software.

## ✨ Features

- **🛡️ Safety First**: Comprehensive backup system with read-only protection
- **🔄 Smart JSON Merging**: Native Python JSON handling for reliable flag combination
- **⚡ Quick Fleasion Mode**: One-click application of Fleasion FastFlag
- **🎨 Modern Interface**: Color-coded terminal interface with clear visual feedback
- **📚 Built-in Help**: Extensive documentation and troubleshooting guides
- **🔐 Administrator Checks**: Automatic privilege detection and elevation prompts
- **🔙 Easy Restoration**: Quick restore functionality from backups
- **🐛 Robust Error Handling**: Detailed error messages and recovery guidance

## 📋 Requirements

- **Python 3.6+** (included with Windows 10/11 or install from [python.org](https://python.org))
- **Windows Operating System**
- **Administrator Privileges**
- **Roblox installed and run at least once**

## 🚀 Installation

### Option 1: Easy Launch (Recommended)
1. **Download** the FastFlagBypass tool to your desired location
2. **Double-click** `run.bat` - it will automatically:
   - ✅ Check for Python installation
   - ✅ Open python.org if Python is missing
   - ✅ Create and activate a virtual environment
   - ✅ Install any required dependencies
   - ✅ Launch the FastFlag tool

### Option 2: Manual Setup
1. **Ensure Python 3.6+ is installed** (Windows 10/11 have it built-in)
2. **Verify Roblox installation** and has been run at least once
3. **Right-click on PowerShell/Command Prompt** and select "Run as administrator"
4. **Navigate** to the tool directory and run:
   ```bash
   python bypass.py
   ```

### 🎯 Recommended: Use `run.bat`
The `run.bat` launcher handles all the complexity for you and provides the best user experience!

## 🎯 Quick Start

### First Time Setup

1. **🔄 Create a Backup** (Option 1)
   - **CRITICAL**: Do this FIRST with clean Roblox settings
   - This protects your original configuration
   - Only create backup once with vanilla settings

2. **⚙️ Apply FastFlags**
   - **Option 2**: Use custom flags from `fastflags.json`
   - **Option 3**: Quick apply Fleasion FastFlag
   - Files become read-only to prevent Roblox interference

3. **🧪 Test Your Setup**
   - Launch Roblox to verify functionality
   - If issues occur, use Option 4 to restore from backup

## 📱 Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| **1** | 🔄 Backup IxpSettings.json | Creates safety backup of original settings |
| **2** | ⚙️ Append FastFlags | Merges custom flags from `fastflags.json` |
| **3** | ⚡ Apply Fleasion FastFlag | Quick-applies `FFlagHttpUseRbxStorage10: false` |
| **4** | 🔙 Restore from backup | Reverts to original backed-up settings |
| **5** | 📚 Help and Instructions | Comprehensive usage documentation |
| **6** | 🚪 Exit | Safely closes the application |

## ⚡ Fleasion FastFlag (Option 3)

The Fleasion FastFlag is specifically used for the **Fleasion app** - a popular Roblox modification tool:

```json
{"FFlagHttpUseRbxStorage10": "false"}
```

**Purpose:**
- Required for Fleasion app functionality
- Disables HTTP RbxStorage10 for Fleasion compatibility
- Essential flag for users running Fleasion modifications

**Usage:**
1. Ensure you have a backup (Option 1)
2. Select Option 3 from the menu
3. Confirm application when prompted

## ⚙️ Custom FastFlags (Option 2)

### Editing fastflags.json

Create your custom FastFlag configuration in `fastflags.json`:

```json
{
  "FFlagDebugForceFutureIsBright": "True",
  "FFlagUserShowGuiHideToggles": "True", 
  "DFIntCanHideGuiGroupId": "0",
  "FFlagHttpUseRbxStorage10": "false"
}
```

### JSON Format Requirements

- ✅ **Valid JSON syntax required**
- ✅ **Use double quotes** for keys and string values
- ✅ **Boolean values**: `"True"` or `"False"` (as strings)
- ✅ **Integer values**: `"0"`, `"1"`, etc. (as strings)
- ❌ **No trailing commas**

## 🔄 Changing FastFlags

To modify your FastFlags safely:

1. **🔙 Restore** from backup (Option 4)
2. **📝 Edit** `fastflags.json` with new settings
3. **⚙️ Apply** updated flags (Option 2 or 3)
4. **🚫 DO NOT** create new backup at this point

## 🛡️ Safety Features

### 🔄 Backup Protection
- Automatic backup validation
- Prevents overwriting clean backups
- Warns about modified settings backup

### 🔒 File Protection
- Sets modified files as read-only
- Prevents Roblox from auto-reverting changes
- Handles file permissions safely

### ⚠️ Error Handling
- Comprehensive error checking with Python's robust exception handling
- Clear, color-coded failure messages
- Safe rollback on errors
- Detailed troubleshooting guidance

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| 🚫 Roblox won't start | Restore from backup (Option 4) |
| ❌ FastFlags not working | Check JSON syntax in `fastflags.json` |
| 🔒 File is locked | Run `run.bat` as administrator |
| 💾 Backup fails | Ensure Roblox installed and run once |
| 🛡️ Permission denied | Right-click `run.bat` → "Run as administrator" |
| 🐍 Python not found | `run.bat` will open python.org automatically |
| 🎨 No colors in terminal | Use Windows Terminal or PowerShell |
| ⚙️ Virtual environment issues | Delete `venv` folder and run `run.bat` again |

## 📁 File Structure

```
FastFlagBypass/
├── run.bat                # 🚀 Easy launcher (NEW! - Recommended)
├── bypass.py              # 🐍 Main Python application
├── requirements.txt       # 📦 Python dependencies
├── bypass.bat             # 📜 Legacy batch file (deprecated)
├── fastflags.json         # ⚙️ Custom FastFlag configuration
├── venv/                  # 🐍 Virtual environment (auto-created)
├── backup/                # 💾 Backup directory
│   └── IxpSettings_backup.json
└── README.md             # 📚 This documentation
```

## 🎯 Target Locations

The tool modifies the following Roblox file:
```
%LocalAppData%\Roblox\ClientSettings\IxpSettings.json
```

## 🔬 Technical Details

- **🐍 Platform**: Python 3.6+ (Windows focused)
- **🔐 Permissions**: Administrator privileges required
- **📋 JSON Processing**: Native Python JSON library
- **🔒 File Protection**: Windows file attributes (read-only)
- **💾 Backup Strategy**: Single clean backup preservation
- **🎨 Interface**: ANSI color codes for enhanced readability

## 🛡️ Security Considerations

- ✅ Always backup before modifications
- 🧪 Test flags individually to identify issues
- ⚠️ Some flags may cause crashes or unexpected behavior
- 🔄 Roblox updates may reset your settings
- 📖 Use with understanding of potential account risks
- 🐍 Python provides better error handling than batch scripts

## 📚 Additional Resources

### 🚩 Common FastFlags

| FastFlag | Purpose | Value |
|----------|---------|-------|
| `FFlagHttpUseRbxStorage10` | Disable HTTP storage | `"false"` |
| `FFlagDebugForceFutureIsBright` | Enable Future lighting | `"True"` |
| `FFlagUserShowGuiHideToggles` | Show GUI toggles | `"True"` |
| `DFIntCanHideGuiGroupId` | Hide GUI elements | `"0"` |

### ✅ JSON Validation

Before applying custom flags, validate your JSON:
- Use online JSON validators like [jsonlint.com](https://jsonlint.com)
- Check for syntax errors
- Ensure proper formatting
- The Python version provides better JSON error reporting

## 🤝 Contributing

Found a bug or have a feature request? Please ensure:
- You've tested with a backup
- You can reproduce the issue
- You've checked the troubleshooting section
- Include Python version and error messages

## 📄 License

This project is released under the MIT License. See `LICENSE` file for details.

## ⚖️ Legal Notice

This tool is for educational and research purposes. Users are responsible for compliance with Roblox Terms of Service and any applicable laws. The authors disclaim all liability for misuse or consequences of this software.

---

**🎯 Remember**: Always backup first, test carefully, and use responsibly!