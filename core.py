from extract.extract import ExtractorWeather
from transform.transform import trasformData
from load.load import loaderS3
from dotenv import load_dotenv

load_dotenv()


class etl:
    data = ExtractorWeather.extract()
    data_addres = trasformData.trasform_data(data)
    loaderS3.loadData(data_addres)


if __name__ == "__main__":
    etl()
