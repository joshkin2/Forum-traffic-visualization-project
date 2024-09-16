import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data by removing the top and bottom 2.5% of page views
df = df[(df['value']>=df['value'].quantile(0.025))& (df['value']<= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax=plt.subplots(figsize=(12,6))
    ax.plot(df.index,df['value'],color='red')
  # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot  # Prepare data for bar plot
    df_bar = df.copy()
   
    # Draw bar plot
    df_bar['year']= df.index.year
    df_bar['month']=df.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
   # Create the bar plot
    fig= df_bar.plot(kind='bar',figsize=(12,6), legend=True).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June','July','August','September','October','November','December'])



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)  # Reset index to move 'date' from index to a column
    df_box['year'] = [d.year for d in df_box.date]   # Extract year
    df_box['month'] = [d.strftime('%b') for d in df_box.date]   # Extract month as abbreviated string

    # Draw box plots (using Seaborn)
    # Sort the months properly for month-wise box plot
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    fig, (ax1, ax2)= plt.subplots(1,2,figsize=(15,7))
    # Year-wise box plot
    sns.boxplot(x='year',y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    # Month-wise box plot
    sns.boxplot(x='month',y='value', data=df_box, ax=ax2, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
