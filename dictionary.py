
def named(**kwargs):
    print(kwargs)


    heights = kwargs.values()


    if heights:
        average_height = sum(heights) / len(heights)
        print(f"Average height: {average_height}")
    else:
        print("No heights provided.")



named(vikash=165, bob= 175, jack= 152)




