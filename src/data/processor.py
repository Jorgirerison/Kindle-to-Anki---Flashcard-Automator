from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
import csv 
import os
from datetime import datetime
import data._api as _api

def criate_execution_registrer():
    """criate a csv with infos about the execucions of the script
    """
    file_csv = 'execution_register.csv'

    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(file_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_date])

    print(f"Anki cards created in {current_date}")

def catch_last_execution():
    """verify if there is file 'execution_register' and return the last registrer
    This function is not literal used, but it's called in df_books_filtered_by_date

    Returns:
        str: date of the last execution of the script
    """
    if not os.path.exists('execution_register.csv'):
      print("ainda não há nenhum registro")
      return  

    with open('execution_register.csv', 'r') as file:
        reader = csv.reader(file)
        row = list(reader)
        if row:
            last_execution = row[-1][0] 
            print(last_execution)
            return last_execution 
        return None
    
def return_df_all_books(metadata, engine):
  """Search and return all books in the kindle

  Args:
      metadata (class): _description_
      engine (class): _description_

  Returns:
      df: return a df with books
  """
  book_info = Table("BOOK_INFO", metadata, autoload_with=engine)

  # Executando consulta e retornando como DataFrame
  with engine.connect() as conn:
      result = conn.execute(book_info.select())
      df = pd.DataFrame(result.fetchall(), columns=result.keys())

  return df

def return_df_books_filtered_by_language(df_books):
    """return a df filtered by language

    Args:
        df_books (df): dataframe of bookks
    """
    df_en = df_books[df_books["lang"] == "en"]
    return df_en
    
def return_df_all_lookups(metadata, engine):
    """Search and reeturn all lookups in the kindle

    Args:
        metadata (class): _description_
        engine (class): _description_

    Returns:
        df: return a df with lookups
    """
    book_info = Table("LOOKUPS", metadata, autoload_with=engine)

    with engine.connect() as conn:
        result = conn.execute(book_info.select())
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df

def return_df_lookups_with_column_format_date(df_lookups):
    """Add a new column that describe the format of date column 'timestamp'
    """
    df_lookups['format_date'] = pd.to_datetime(df_lookups['timestamp'], unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')

    return df_lookups

def return_df_lookups_filtered_by_date(df_lookups):
    """return a df filtered by date

    Args:
        df_lookups (df): dataframe of lookups

    Returns:
        df: df filtered
    """
    last_execution = catch_last_execution()
    if last_execution:
        filtered_date_df = df_lookups[df_lookups["format_date"] > last_execution]
        return filtered_date_df
    else:
        return df_lookups
    
def return_id_choice_book(df_en):
    """input for the choice of user about the book

    Args:
        df_en (df): df filtered by language

    Returns:
        id: if of the book
    """
    if df_en.empty:
        print("There is no book in this language")
        return None
    
    for i, title in enumerate(df_en["title"].values, 1):
        print(f"{i}. {title}")  
    
    while True:
        escolha = input("\nWrite the number of title (or '0' for cancel): ").strip()
        
        if escolha == '0':
            print("Cancel selection")
            return None
        
        if escolha.isdigit() and 1 <= int(escolha) <= len(df_en):
            selected_row = df_en.iloc[[int(escolha) - 1]]
            id_selected_row = selected_row["id"].item()
            return id_selected_row

        
        print("Invalid option. Try again.")

def return_df_across_books_with_lookups(id, df_lookups):
    """return the df filtered by id choised for the user

    Args:
        id (str): id choised in the previous function
        df_lookups (df): df lookups with any modifications

    Returns:
       df: df filtered by id
    """
    return df_lookups[df_lookups["book_key"] == id]

def return_df_lookups_adjusted_on_collum_word_key(df_lookups):
    """format content of column word usually

    Args:
        df_lookups (df): df lookups with any modfications

    Returns:
        df: df with column 'word_key' withdrawn ':en'
    """
    df_lookups.loc[:,"word_key"] = df_lookups["word_key"].str.split(":", n=1).str[1]
    return df_lookups

def return_csv_on_model_frpg(df, api_key, words_data=[]):
    """return a csv on model frpg criated by ELiezer Piano, but you can get yourself model

    Args:
        df (df): df_acrossing
        words_data (list, optional): Defaults to [].
    """
    for index, row in df.iterrows():
        word = row["word_key"]
        word_data = _api.search_info(word)

        if word_data:
            word_data["setence"] = row["usage"]
            word_data["translate"] = _api.google_translate(api_key, row["usage"])
            word_data["definition"] = _api.google_translate(api_key, word_data["definition"])
            print(word_data)
            words_data.append(word_data)
        else:
            pass

    df_export_2_anki = pd.DataFrame(words_data)
    df_export_2_anki.to_csv("saida.csv", index=False, encoding='utf-8')