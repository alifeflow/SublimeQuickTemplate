# SublimeQuickTemplate
QuickTemplate plugin for Sublime Text 3

This plugin allows you to create a new file from a template by simply typing a command after pressing shift+ctrl+p. Date macro in the template file will substitute with the current date.

## How to Install

This plugin has not been uploaded to any package repo, which means you will have to spend a little effort on installing manually. But installing is EASY.

Open Sublime Text 3. Click Preferences -> Browse Packages. A file explorer will pop up. Open User folder and copy the files downloaded here. Remember to unzip if they are in a zip file.

It's DONE.

## How to Use

To use this plugin, you have to setup customized commands for Sublime Text and write the corresponding template files.

### Customize Commands

Click Preferences -> Browse Packages. A file explorer will pop up. Open User folder. Then open the QuickTemplate.sublime-commands file.

A customized command looks like this:

```
{
		"caption": "Template: New Diary",
		"command": "new_template_from_file",
		"args": {"file": "D:\\OneDrive\\iA Writer\\Diary\\_Template.md",
			"type": "md",
			"syntax": "Packages/MarkdownHighlighting/Markdown.sublime-syntax",
			"fileLocString": "D:\\OneDrive\\iA Writer\\Diary\\"
		}
	},

```

Please change the string after "file": to the file location of your template file. And change the "type", "syntax" correspondingly. Usually, change the "Markdown" in "/Markdown.sublime-syntax" to Java or other language type will work. Finally, change the "fileLocString ": to the place you would like to store the file. You may delete the line of "fileLocString": "D:\\OneDrive\\iA Writer\\Diary\\" if you would like new file being stored dynamically into the folder opened in Sublime Text.

### Writing Template Files

Here is a brief template file for my diary:

```
@date
# @date
## On Work

## On Life

## On Self-Hosted Work

## New Ideas

## Books Read

## Others
```

Auto substitution will happen to the string started with @. Here, @date will be substituted with the current date.

The rest will remain unchanged.

## Need new function?

Just post an issue in  [this project](https://github.com/alifeflow/SublimeQuickTemplate/issues). I will do the rest of the work.