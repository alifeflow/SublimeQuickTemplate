import sublime, sublime_plugin
import datetime, os

class new_from_thisCommand(sublime_plugin.WindowCommand):
	def run(self, edit = None):
		view = sublime.active_window().active_view()

		type = view.file_name().split('.')[-1]
		lines = view.substr(sublime.Region(0, view.size()))
		syntax = view.settings().get('syntax')
		print(syntax)

		new_from_string(lines, type, syntax)

class new_diaryCommand(sublime_plugin.WindowCommand):
	def run(self, edit = None):
		new_from_file("D:\\OneDrive\\iA Writer\\Diary\\_Template.md", "md", "Packages/MarkdownHighlighting/Markdown.sublime-syntax", "D:\\OneDrive\\iA Writer\\Diary\\")

class new_template_from_fileCommand(sublime_plugin.WindowCommand):
	def run(self, file, type, syntax, fileLocString = None, edit = None):
		new_from_file(file, type, syntax, fileLocString)

def new_from_file(file, type, syntax, fileLocString = None):
	file = open(file,'r')
	new_from_string(file.read(), type, syntax, fileLocString)

def new_from_string(fileStrings, type, syntax, fileLocString = None):
	view = sublime.active_window().active_view()

	fileStrings = parse_format(fileStrings).split("\n",1)
	title = fileStrings[0]
	lines = fileStrings[1]

	if fileLocString is None:
		set_code(creat_tab(view, title, type), lines, syntax)
	else:
		fileNameString = os.path.join(fileLocString, title+"."+type)
		if (not os.path.exists(fileNameString)):
			try:
				file_write = open(fileNameString, 'w')
				file_write.write(lines)
			finally:
				file_write.close()
		sublime.active_window().open_file(fileNameString)


def parse_format(line):
	date = datetime.datetime.now().strftime('%Y-%m-%d')
	return line.replace('@date', date)

def creat_tab(view, title, type):
	win = view.window()
	tab = win.new_file()
	tab.set_name(title+"."+type)
	return tab

def set_code(tab, code, syntax):
	# tab.set_name('untitled.' + self.type)
	# insert codes
	tab.run_command('insert_snippet', {'contents': code})
	tab.set_syntax_file(syntax)
