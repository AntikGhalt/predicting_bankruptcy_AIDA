import pandas as pd
import numpy as np
import re

def example():
    data = {
        'Tax code number': ['A1', 'B2'],
        'Company Name': ['Alpha', 'Beta'],
        'Revenue 2013': [100, 200],
        'Revenue 2014': [110, 210],
        'Event 1': ['bankruptcy', 'none'],
        'Date of open Event 1': ['2014-06-01', None],
    }
    final_df = pd.DataFrame(data)
    # begin reshape long code
    year_pattern = re.compile(r'(20\d{2})$')
    wide_cols = [c for c in final_df.columns if year_pattern.search(c)]
    id_cols = [c for c in final_df.columns if c not in wide_cols]
    long_df = final_df.melt(
        id_vars=id_cols,
        value_vars=wide_cols,
        var_name='variable',
        value_name='value'
    )
    long_df['Year'] = long_df['variable'].str.extract(year_pattern)
    long_df['variable'] = long_df['variable'].str.replace(r'\s*20\d{2}$', '', regex=True)
    long_df = (
        long_df
        .pivot_table(index=id_cols + ['Year'], columns='variable', values='value', aggfunc='first')
        .reset_index()
    )
    name_col = 'Company Name'
    key_col = 'Tax code number'
    long_df['NameYear'] = long_df[name_col].astype(str) + ' ' + long_df['Year']
    long_df['KeyYear'] = long_df[key_col].astype(str) + ' ' + long_df['Year']

    bank_year = pd.Series(index=final_df.index, dtype='float')
    for col in [c for c in final_df.columns if c.startswith('Event ')]:
        mask = final_df[col].str.contains('bankruptcy', case=False, na=False)
        m = re.search(r'(-?\d+)', col)
        if not m:
            continue
        idx = m.group(1)
        date_col = f'Date of open Event {idx}'
        year = pd.to_datetime(final_df.get(date_col), errors='coerce').dt.year
        bank_year = bank_year.where(~mask, year)
    bank_df = pd.DataFrame({key_col: final_df[key_col], 'bankruptcy_year': bank_year})
    long_df = long_df.merge(bank_df, on=key_col, how='left')
    long_df = long_df[(long_df['bankruptcy_year'].isna()) | (long_df['Year'].astype(float) <= long_df['bankruptcy_year'])]
    print(long_df)

if __name__ == '__main__':
    example()
