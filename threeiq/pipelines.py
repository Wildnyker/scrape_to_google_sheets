# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ThreeiqPipeline:
    def process_item(self, item, spider):
        import gspread
        gc = gspread.service_account(filename='')  # creating credentials - you should add here a json file which you get from googlr api
        sh = gc.open_by_key('')  # giving the spreadheet_id - you should add
        # your spreadsheet id from google sheets
        worksheet = sh.sheet1  # getting a defined sheet from spreadsheet
        results = worksheet.get_all_records()  # getting all the results ogf it
        worksheet.update("A1", [["Cashname"], [item['Cashname']]])
        worksheet.update("B1", [["Cashvalue"], [item['Cashvalue']]])
        print(results)
        return item
