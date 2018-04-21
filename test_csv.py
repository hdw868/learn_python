import csv


# # define header
# header_list = ['Seq', 'Data_source', 'Init_env', 'Restore_md', 'Restore_wh', 'Update_db',
#                'Run_test', 'Destory_wh', 'Total']
# header_str_list = [('%8s\t' % (header)) for header in header_list]
# header_str = (''.join(header_str_list) + '\n')
# # define row
# time_list = [100.22, 200.44, 300, 400.22, 100.56, 900]
# total = sum(time_list)
# time_list.append(total)
# row_str_list = [('%8s\t' % (time)) for time in time_list]
# row_str = (''.join(row_str_list) + '\n')
# data_source = 'MySQL'
#
# # generate avg
# # avg_list = sum(type_time)/len(type_time)
#
# with open('perf_watcher.csv', mode='r+') as f:
#     lien_num = len(f.readlines())
#     # f.write(header_str)
#     f.write('%8s\t' % (lien_num) + '%8s\t' % (data_source) + row_str)
#     f.seek(0)
#     rows = f.readlines()
#     for row in rows:
#         items = row.split()
#         print('items: ' + str(items))
