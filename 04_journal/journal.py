import os
"""
This is the journal module
"""


def load(name):
    """
    This method creates and loads a new journal

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """

    journal_data = []

    filename = get_full_path(name)
    if os.path.exists(filename):
        print('....Loading Journal {}'.format(name))
        with open(filename, 'r') as current_entries:
            for entry in current_entries:
                journal_data.append(entry.rstrip())
    else:
        print('Journal {} does not exit'.format(name))

    return journal_data


def get_full_path(name):
    """
    Creates absolute path for the given name. OS independent

    :param name: The name of the journal
    :return: The absolute pathway for the journal file
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def save(name, journal_data):
    """
    Saves Journal Data to a .jls file with given name

    :param name: name of the journal file
    :param journal_data: data to save

    """
    filename = get_full_path(name)
    print('...... saving to: {}'.format(filename))
    with open(filename, 'w') as fout:

        for entry in journal_data:
            fout.write('{}\n'.format(entry))


def add_entry(text, journal_data):
    """
    Adds a new entry to the journal

    :param text: new data to add
    :param journal_data: current journal data
    """
    journal_data.append(text)
