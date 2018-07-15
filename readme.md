
# Small Python scripts 

### Adding cover image to mp3 file
* [add_cover_img_to_mp3.py](https://github.com/TianaQ/python-scripts/blob/master/add_cover_img_to_mp3.py)  

I found some audiobooks for my little son that were on vinil in my childhood. But he couldn't select a specific title in a playlist because he couldn't read yet. So I decided to add cover images of the records to the mp3 files I had. Maybe, you need that too?

Put your mp3 files and jpg or png files in a directory (it may be the same directory for all files). Use the same names for an mp3 file and the corresponding image. Save the script file to your computer and use Terminal/CMD to launch it

```
	$ python path_to_the_script_directory_goes_here/add_cover_img_to_mp3.py path_to_mp3 path_to_img
```
or
```
	$ python path_to_the_script_directory_goes_here/add_cover_img_to_mp3.py
```
If you didn't provide the paths to mp3 files and images on launching, the script will ask for them later.

**Warning**: existing audio tags will be cleared by the script



### Readind csv files from a directory into pandas DataFrame and .csv file
* [dir_to_df_and_csv.py](https://github.com/TianaQ/python-scripts/blob/master/dir_to_df_and_csv.py)

Launch the script from the command line with the path to the data directory with csv files
```
	$ python path_to_script_directory/dir_to_df_and_csv.py path_to_data_dir
```
or enter the path when asked for input by the script.

If you want to extract only specific columns, change this part of code as described in comments

```
	# if you need only specific columns, list their names within the brackets: ['column_1', 'column_2', 'etc']
	# if you want to keep the order of columns, list all of them in brackets
	col_names = []
```

The script will create pandas Dataframe and write it to *data_dir.csv* file in the folder where the data directory is stored.