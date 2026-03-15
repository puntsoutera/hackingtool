import os

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a platform that is used by Cyber Investigators.\n" \
                  "[!] Works in any OS\n" \
                  "[!] Recover Deleted Files from any OS & Media \n" \
                  "[!] Extract Image Metadata"
    RUN_COMMANDS = ["sudo autopsy"]

    def __init__(self):
        super().__init__(installable=False)


class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what’s happening in your network.\n " \
                  "And also investigate Network related incident"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super().__init__(installable=False)


class BulkExtractor(HackingTool):
    TITLE = "Bulk extractor"
    DESCRIPTION = "Extract useful information without parsing the file system"
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__([
            ('GUI Mode (Download required)', self.gui_mode),
            ('CLI Mode', self.cli_mode)
        ], installable=False, runnable=False)

    def gui_mode(self):
        import subprocess
        from config import get_tools_dir
        console.print(Panel(Text(self.TITLE, justify="center"), style="bold magenta"))
        console.print("[bold magenta]Cloning repository and attempting to run GUI...[/]")
        tools_dir = get_tools_dir()
        subprocess.run(["git", "clone", "https://github.com/simsong/bulk_extractor.git"],
                       cwd=str(tools_dir))
        be_dir = tools_dir / "bulk_extractor"
        subprocess.run(["./BEViewer"], cwd=str(be_dir / "java_gui"))
        console.print(
            "[magenta]If you get an error after clone go to /java_gui/src/ and compile the .jar file && run ./BEViewer[/]")
        console.print(
            "[magenta]Please visit for more details about installation: https://github.com/simsong/bulk_extractor[/]")

    def cli_mode(self):
        import subprocess
        console.print(Panel(Text(self.TITLE + " - CLI Mode", justify="center"), style="bold magenta"))
        subprocess.run(["sudo", "apt", "install", "-y", "bulk-extractor"])
        console.print("[magenta]bulk_extractor [options] imagefile[/]")
        subprocess.run(["bulk_extractor", "-h"])


class Guymager(HackingTool):
    TITLE = "Disk Clone and ISO Image Acquire"
    DESCRIPTION = "Guymager is a free forensic imager for media acquisition."
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt install guymager"]
    RUN_COMMANDS = ["sudo guymager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"

    def __init__(self):
        super().__init__(installable=False)


class Toolsley(HackingTool):
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley got more than ten useful tools for investigation.\n" \
                  "[+]File signature verifier\n" \
                  "[+]File identifier \n" \
                  "[+]Hash & Validate \n" \
                  "[+]Binary inspector \n " \
                  "[+]Encode text \n" \
                  "[+]Data URI generator \n" \
                  "[+]Password generator"
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super().__init__(installable=False, runnable=False)


class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic tools"
    TOOLS = [
        Autopsy(),
        Wireshark(),
        BulkExtractor(),
        Guymager(),
        Toolsley()
    ]

if __name__ == "__main__":
    tools = ForensicTools()
    tools.show_options()
