# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        name = item['name']
        itemId = name + item['itemId']
        parentId = name + item['parentId']
        skuName = item['skuName']
        price = item['price']
        img_src = item['img_src']

        self.path = name
        self.item_path = os.path.join(self.path, parentId)
        self.picture_path = os.path.join(self.item_path, '图片')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if not os.path.exists(self.item_path):
            os.mkdir(self.item_path)
        if not os.path.exists(self.picture_path):
            os.mkdir(self.picture_path)
        with open('products_backup.csv', 'a') as f:
            f.write(name + ',' + itemId + ',' + skuName + ',' + price + '\n')

        with open(self.item_path + '/params.csv', 'w') as f:
            f.write(item['property'] + '\n')

        i = 1
        images = []
        for imgUrl in img_src:
            imgUrl = imgUrl.replace('60w_60h', '400w_400h')
            images.append(imgUrl)
            image = requests.get(imgUrl, stream=True)
            with open(self.picture_path + "/" + itemId+ "_" + str(i) + ".jpg", "wb") as jpg:  # 保存图片
                for chunk in image:
                    jpg.write(chunk)
            i = i + 1

        with open(self.item_path + '/' + parentId + '_comments.csv', 'a') as f:
            comment_list = item['comment_list']
            #f.write('用户名,评论id,评论时间,点赞数,商品分数,内容\n')
            for comment in comment_list:
                f.write(comment[3] + ',' + comment[0] + ',' + comment[2] + ',' + comment[5] + ',' + comment[4] + ',' + comment[1] + '\n')
        return item
