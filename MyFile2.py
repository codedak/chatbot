from Tkinter import *
import execute
import tensorflow as tf


def FilteredMessage(EntryText):
    """
    Filter out all useless white lines at the end of a string,
    returns a new, beautifully filtered string.
    """
    EndFiltered = ''
    for i in range(len(EntryText) - 1, -1, -1):
        if EntryText[i] != '\n':
            EndFiltered = EntryText[0:i + 1]
            break
    for i in range(0, len(EndFiltered), 1):
        if EndFiltered[i] != "\n":
            return EndFiltered[i:] + '\n'
    return ''



def LoadMyEntry(ChatLog, EntryText,sess, model, enc_vocab, rev_dec_vocab):
    s = execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, EntryText)
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end')) - 1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber + 0.4)
            ChatLog.tag_config("You", foreground="#FF3300", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
    LoadJkEntry(ChatLog, s)


def LoadJkEntry(ChatLog, EntryText2):
    if EntryText2 != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            try:
                LineNumber = float(ChatLog.index('end')) - 1.0
            except:
                pass
            ChatLog.insert(END, "Victor: " + EntryText2 +'\n')
            ChatLog.tag_add("Victor: ", LineNumber, LineNumber + 0.6)
            ChatLog.tag_config("Victor: ", foreground="#04B404", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
