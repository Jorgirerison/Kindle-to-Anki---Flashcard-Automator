from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData, Table

import sys
sys.path.append(".")
from data import _api
from src.data import processor

def main():
  load_dotenv('.env')
  api_key = os.getenv('API_KEY')
  engine = create_engine('sqlite:///vocab.db')
  metadata = MetaData()
  metadata.reflect(bind=engine)
  #all of the books
  df_books = processor.return_df_all_books(metadata, engine)
  df_books_en = processor.return_df_books_filtered_by_language(df_books)
  id_of_book = processor.return_id_choice_book(df_books_en)
  #all of the lookups
  df_lookups = processor.return_df_all_lookups(metadata, engine)
  df_with_format_date = processor.return_df_lookups_with_column_format_date(df_lookups)
  df_lookups_filtered_by_date_last_execution_of_script = processor.return_df_lookups_filtered_by_date(df_with_format_date)
  df_lookups_column_wordkey_adjusted = processor.return_df_lookups_adjusted_on_collum_word_key(df_lookups_filtered_by_date_last_execution_of_script)
  #interaction between books and lookups
  df_crossing_books_with_lookups = processor.return_df_across_books_with_lookups(id_of_book, df_lookups_column_wordkey_adjusted)
  try:
    processor.return_csv_on_model_frpg(df_crossing_books_with_lookups, api_key)
    processor.criate_execution_registrer()
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
