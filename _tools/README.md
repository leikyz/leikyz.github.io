# Tools

## generate_project_pages.py

Regenerates all HTML files in `projects/` from the `PROJECTS` dict at the top of the script.

To add or edit a project:
1. Edit the `PROJECTS` list in the script (or add a new entry).
2. Run: `python3 _tools/generate_project_pages.py`
3. Output goes to `projects/`.

To wire a new project into the homepage IDE workspace, edit `index.html`:
- Add an entry inside one of the `<ul class="ide-file-list">` panels (or to the Featured panel).
- Update the `ide-tab-count` number on the corresponding tab.
- Update the statusbar count at the bottom of the workspace.
