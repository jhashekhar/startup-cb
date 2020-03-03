import matplotlib.pyplot as plt
import seaborn as sns
import utils



# display funding and status of the adjoining start-ups

def pie_plot(titles, *args):
    # args: currently it takes in an input in the form of " a defaultdict wraped in a list" 
    explode = (0.0, 0.1, 0.1)
    _, ax = plt.subplots(1, len(args[0]), figsize=(16, 6))

    if len(args[0]) > 1:
        for i in range(len(args[0])):
            
            ax[i].set_title(titles[i])
            ax[i].pie(args[0][i]['sizes'], explode=explode, labels=args[0][i]['labels'], autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()


    elif len(args[0]) == 1:
        
        ax.set_title(titles)
        ax.pie(args[0]['sizes'], explode=explode, labels=args[0]['labels'], autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()        



def bar_plot(titles, *args):
    return





# plot pie charts for percentage of operating, acquired, closed
def status_plot(df, markets, d):
    #dic1 = {'labels': status, 'sizes': utils.status_per_market(df, market, status)}
    pie_plot(markets, d)


def funding_plot(df, markets, d):
    pie_plot(markets, d)





'''
def show_plots(dic1, dic2):

    explode = (0.0, 0.1, 0.1)
    _, ax = plt.subplots(1, 2, figsize=(10, 6))
    
    ax[0].pie(dic1['sizes'], explode=explode, labels=dic1['labels'], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


    ax[1].pie(dic2['sizes'], explode=explode, labels=dic2['labels'], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax[1].axis('equal')
    
    
    
    plt.show()

'''