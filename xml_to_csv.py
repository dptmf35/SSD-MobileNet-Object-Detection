import os
import glob
import pandas as pd
img_width = 320
img_height = 240
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        filename = os.path.basename(xml_file).replace('.xml', '.jpg')
        with open(xml_file, 'r') as file:
            for line in file.readlines():
                parts = line.strip().split()
                    
                if len(parts) == 5:
                    class_id, x_center, y_center, width, height = parts
                    # 값을 이미지 크기에 따라 스케일링
                    x_center = float(x_center) * img_width
                    y_center = float(y_center) * img_height
                    width = float(width) * img_width
                    height = float(height) * img_height
                    
                    xmin = int(x_center - width / 2)
                    ymin = int(y_center - height / 2)
                    xmax = int(x_center + width / 2)
                    ymax = int(y_center + height / 2)
                    # class_id를 int로 변환
                    class_id = int(class_id)

                    if class_id >= 2 :
                        continue

                    # filename, width, height, class_id, xmin, ymin, xmax, ymax 형식으로 저장
                    value = (filename,
                             320,  # 이미지 너비
                             240,  # 이미지 높이
                             class_id,
                             xmin,
                             ymin,
                             xmax,
                             ymax)
                    xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train_data', 'test_data']:
        image_path = os.path.join(os.getcwd(), '{}'.format(directory))
        print(image_path)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')

if __name__ == "__main__":
    main()

# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET


# def xml_to_csv(path):
#     xml_list = []
#     for xml_file in glob.glob(path + '/*.xml'):
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      member[0].text,
#                      int(member[4][0].text),
#                      int(member[4][1].text),
#                      int(member[4][2].text),
#                      int(member[4][3].text)
#                      )
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     return xml_df


# def main():
#     for directory in ['train_data','test_data']:
#         image_path = os.path.join(os.getcwd(), '/{}'.format(directory))
#         print(image_path)
#         xml_df = xml_to_csv(image_path)
#         xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
#         print('Successfully converted xml to csv.')


# main()
