import PySimpleGUI as Sg


def layout() -> list:
    """
    Create layout for main window

    :param: None
    :return: None
    :rtype: None
    """

    gui = [
        [Sg.Text('URL:'),
         Sg.InputText(key='-url-', size=(95, 1))],
        [Sg.Text('Save Folder:'),
         Sg.InputText(key='-save_folder-', readonly=True, size=(80, 1)),
         Sg.FolderBrowse()],
        [Sg.Checkbox('PNG', key='-png-', default=True),
         Sg.Checkbox('JPG', key='-jpg-', default=True),
         Sg.Button('Run', key='-run-', size=(8, 1))],
        [Sg.HSeparator()],
        [Sg.Multiline(size=(100, 15), disabled=True, autoscroll=True, reroute_stdout=True, reroute_stderr=True)]
    ]

    return gui


def main():
    window = Sg.Window('Image Downloader', layout())

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == Sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        if event == '-run-':
            types = []
            url = values['-url-']
            save_folder = values['-save_folder-']

            if len(url) == 0:
                Sg.Popup('Missing URL')
                continue

            if len(save_folder) == 0:
                Sg.Popup('Folder not selected')
                continue

            if values['-png-']:
                types.append('png')

            if values['-jpg-']:
                types.append('jpg')


if __name__ == '__main__':
    main()
