from xlsxwriter.utility import xl_cell_to_rowcol, xl_rowcol_to_cell

# several functions wich helps to do some common
# operations related to saving to excel documents

def add_sheet(xl_writer, sheet_name):
    '''Adding a sheet with setted name.
    Illegal characters will be removed.
    If name is too long it will be cutted.
    If there is same names they will be numerated.'''
    # inputs:
    # xl_writer - xlsx writer wich must contains new list
    # sheet_name -  desired name of creating sheet,
    #               it can be changed by method, in case
    #               incorrect symbols, too long name or
    #               recurring name  
        
    sheet_name = sheet_name.replace('/', ' ')
    sheet_name = sheet_name if len(sheet_name) < 31 else sheet_name[0:31]
        
    final_name = sheet_name
    i = 2
    # if the name is too long or repeating many times
    # its need spesical handle for this cases
    while final_name in xl_writer.sheets.keys():
        i_str = str(i)
        final_name = sheet_name + i_str

        if len(final_name) >= 32:
            final_name = final_name[0:(31-len(i_str))] + final_name[31:]

        i += 1
        
    result_sheet = xl_writer.book.add_worksheet(final_name)
    xl_writer.sheets[final_name] = result_sheet
        
    return final_name


def save_double_column_df(df, xl_writer, startrow = 0, **kwargs):
    '''Function to save doublecolumn DataFrame, to xlwriter'''
    # inputs:
    # df - pandas dataframe to save
    # xl_writer - book for saving
    # startrow - row from wich data frame will begins
    # **kwargs - arguments of `to_excel` function of DataFrame`
    df.drop(df.index).to_excel(xl_writer, startrow = startrow, **kwargs)
    df.to_excel(xl_writer, startrow = startrow + 1, header = False, **kwargs)