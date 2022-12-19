# DS_common
Solutions of my common tasks in DS sphere. Supposed to be used primarily as a submodul.

It contains the following groups:

# visualisation
Funcitons which solve some problems associated with data visualisation.
Examples here: https://github.com/Dranikf/DS_common/blob/main/visualisations_test.ipynb

- **get_meshtraces** - helps to get arguments for `set_traces` method of figure with using `numpy.meshgrid`;
- **pltl_dual_side_arrow** - get list of annotations wich helps to build dual side arrows.

# data_description

Functions which will help to show data in nice form. Examples can be found here: https://github.com/Dranikf/DS_common/blob/main/data_description.ipynb

- **get_col_av_values** - Get availible values in getted column. Makes different for numeric dtypes and others. For numeric dtypes returns range like "[min, max]". For non-numeric dtypes returns possible values;
- **get_col_obj_unique_count** - for non-numeric pandas.Series, returns a count of unique values; for numeric variables returns "-";
- **get_Dran_col_descr** - Return the panas.Series most complete description specified for me;
- **get_most_freq** - returns value from series which has the most frequent manifestation of the trait specified in cond;
- **ECDFs_by_classes** - statsmodels.distributions.empirical_distribution.ECDF wrapper which allows to build different ecdfs for different classes.

# emissions

Functions which helps to deal with emissions in data. Examples can be found here: https://github.com/Dranikf/DS_common/blob/main/emissions_test.ipynb

- **get_frame_quantiles_25_75** - for `pandas.Series` column returns 25% and 75% persentiles;
- **get_selcond_emiss_25_75** - for `pandas.Series` helps to get selection condition according to simple emission detection rule <img src="https://latex.codecogs.com/gif.latex?[x_{25}-b(x_{75}-x_{25});x_{75}+b(x_{75}-x_{25})]"/>, every observation outside this range will be interpreted as emission.

# excel_writing

Functions which deal with excel files. Usually can be used in a combination with `xlsxwriter` library. Examples can be found here: https://github.com/Dranikf/DS_common/blob/main/excel_writing_test.ipynb

- **add_sheet** - adding new sheet into getted excel writer. Get rid of the problems associated with restrictions on the characters used, the length of the name and repetitive names. Duplicate names will be numerated, too long names will be cutted, wrong simbols will be removed from names;
- **save_double_column_df** - by default `pandas` saves multiindex column with some empty cells, this method helps to avoid this problem.


# data processing

Functions which sepeed up data processing. Examples can be found here: https://github.com/Dranikf/DS_common/blob/main/data_processing.ipynb.

- **insert_next** - quick insertion following the column selected by name for pandas.DataFrame;
- **get_num_cond** - get condition for selection from pandas.DataFrame numeric data types;
- **pd_OHE** - one hot encoding for pandas.DataFrame. Result type steel pandas.DataFrame and columns have readable names, in fomat colname_catname;
- **get_merge_repl_rule** - get a merging rule for the levels of some variable for further use in `pandas.Series.replace`;
- **np_replace** - for `numpy.array` replace values, by roole defined as dictionary;
- **fix_pd_multiIndex** - changes `Unnamed` to empty line string in pandas multiIndex.