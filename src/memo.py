import PySimpleGUI as sg

# GUI共通設定
def generalSetting() :
    return sg.theme('DarkTeal9')

# メモアプリの要素を作成する
def createMemoLayout(eventName) :
    layout= [[sg.Text("Add your Memo")],
             [sg.Input(key='-INPUT-')],
             [sg.Text(size=(40,1), key='-OUTPUT-')],
             [sg.Button(s) for s in eventName]]

    return layout

#　Add, Removeボタンクリック時の動作
def updateMemo(window, inputVal) :
    window['-OUTPUT-'].update(inputVal)

# GUI起動
def startGUI() :
    sg = generalSetting()
    # GUIで利用するイベントのハンドラ
    useEvent = {'Add': updateMemo, 'Remove': updateMemo, 'Quit': quit}

    window = sg.Window('SimpleMemo', createMemoLayout(useEvent.keys()),
                        resizable=True, no_titlebar= True)

    while True: 
        event, values = window.read()
        inputVal = '' if event == "Remove" else values['-INPUT-']

        if event != 'Quit': 
            useEvent[event](window, inputVal)
        else :
            window.close()
            break

startGUI()