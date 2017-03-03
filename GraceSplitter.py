# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-02-24 15:27:20
# @Last Modified time: 2017-03-03 18:53:01

import os

import subprocess

import time

import sublime

import sublime_plugin


class GraceSplitterSfkKnifeCommand(sublime_plugin.TextCommand):
    """grace_splitter_sfk_knife command.

    Swiss File Knife split utility —
    http://stahlworks.com/dev/index.php?tool=split
    Default command — “sfk, split, 100k, -yes, -text <current file>”

    Extends:
        sublime_plugin.TextCommand

    """

    def run(self, edit):
        current_file = self.view.file_name()
        if current_file:
            command = ["sfk", "split", "100k", "-yes", "-text", current_file]
            print(command)
            # Run Sublime Text command —
            subprocess.Popen(command, shell=True)
            self.view.close()
        if not current_file:
            return


class GraceSplitterSfkKnifeDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print(GraceSplitterSfkKnifeCommand.__doc__)

# ----------------------------------------------------------------


class GraceSplitterSplitAndOpenLastCommand(sublime_plugin.TextCommand):
    """grace_splitter_split_and_open_last command.

    This command

    + split current file,
    + close current file,
    + open last splitted file.

    Work for “sfk, split, 100k, -yes, -text <current file>”
    split command. If you want support another command, you may write me.
    Using Swiss File Knife split utility —
    http://stahlworks.com/dev/index.php?tool=split

    Extends:
        sublime_plugin.TextCommand

    """

    def run(self, edit):
        current_file = self.view.file_name()
        # Get folder of open file
        current_folder = os.path.dirname(self.view.file_name())
        if current_file:
            command = ["sfk", "split", "100k", "-yes", "-text", current_file]
            print(command)
            # Run Sublime Text command —
            # http://bit.ly/run_windows_shell_in_sublime_text
            subprocess.Popen(command, shell=True)
            self.view.close()

            # Get absolute paths of all files in folder —
            # http://stackoverflow.com/a/21207590/5951529
            list_of_files = [
                os.path.join(
                    current_folder,
                    fn) for fn in next(
                    os.walk(current_folder))[2]]
            # Get file with latest data of creation —
            # http://stackoverflow.com/a/39327156/5951529
            latest_file = max(list_of_files, key=os.path.getctime)
            # Time delay. Otherwise, current file may open again.
            # http://stackoverflow.com/a/510351/5951529
            time.sleep(1)
            print(latest_file)
            sublime.active_window().open_file(latest_file)

        if not current_file:
            return


class GraceSplitterSplitAndOpenLastDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print(GraceSplitterSplitAndOpenLastCommand.__doc__)

# ----------------------------------------------------------------


class GraceSplitterGfsplitCommand(sublime_plugin.TextCommand):
    """grace_splitter_gfsplit command.

    Goetz"s File Splitter —
    http://www.lawrencegoetz.com/programs/gfsplit.htm
    Default command: “gfsplit, <current file>, <current file>, 100”

    Extends:
        sublime_plugin.TextCommand

    """

    def run(self, edit):
        current_file = self.view.file_name()
        if current_file:
            command = ["gfsplit", current_file, current_file, "100"]
            print(command)
            subprocess.Popen(command, shell=True)
            self.view.close()
        if not current_file:
            return


class GraceSplitterGfsplitDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print(GraceSplitterGfsplitCommand.__doc__)

# -----------------------------------------------------------------


class GraceSplitterSplitCommand(sublime_plugin.TextCommand):
    """grace_splitter_split command.

    GNUCoreUtils, split utility —
    http://superuser.com/a/731145/572069
    Default command: “split, <current file>, -d, -l, 2500”
    Use, if you want split file to lines number, not file size.
    Default command — you want get files with 2500 lines in output.

    Extends:
        sublime_plugin.TextCommand

    """

    def run(self, edit):
        current_file = self.view.file_name()
        if current_file:
            command = ["split", current_file, "-d", "-l", "2500"]
            print(command)
            subprocess.Popen(command, shell=True)
            self.view.close()
        if not current_file:
            return


class GraceSplitterSplitDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print(GraceSplitterSplitCommand.__doc__)

# -----------------------------------------------------------------


class GraceSplitterCustomSplitterCommand(sublime_plugin.TextCommand):
    """grace_splitter_custom_splitter command.

    Custom command for file splitting.
    Set your custom command of your preferable file splitter
    in User/GraceSplitter.sublime-settings file.
    Example:
    {
        "gracesplitter_cmd_options": "sfk split 4147k"
    }

    Extends:
        sublime_plugin.TextCommand
    """

    def run(self, edit):

        current_file = self.view.file_name()
        if current_file:
                # Get Sublime Text settings —
                # http://stackoverflow.com/a/14186945/5951529
            settings = sublime.load_settings(
                "Grace_Splitter.sublime-settings")
            cmd_options = settings.get(
                "gracesplitter_cmd_options")
            # Split settings — http://stackoverflow.com/a/743824/5951529
            # http://bit.ly/variable_in_another_variable
            command = cmd_options.split() + [current_file]
            print(command)
            subprocess.call(command, shell=True)
            self.view.close()
        if not current_file:
            return


class GraceSplitterCustomSplitterDocsCommand(
        sublime_plugin.TextCommand):

    def run(self, edit):
        print(GraceSplitterCustomSplitterCommand.__doc__)
