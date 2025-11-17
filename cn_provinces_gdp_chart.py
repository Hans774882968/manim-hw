import pandas as pd
import bar_chart_race as bcr


def main():
    df = pd.read_csv(r'assets\cn_provinces_gdp_chart\cn_provinces_gdp_chart.csv', index_col='year')
    bcr.bar_chart_race(
        df,
        r'media\bili\cn_provinces_gdp_chart\cn_provinces_gdp_chart.mp4',
        title='中国各省份 GDP TOP10（2019-2023）',
        shared_fontdict={'family': 'SimHei'},
    )


if __name__ == '__main__':
    main()
