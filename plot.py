import pandas
import plotly.express as px

df = pandas.DataFrame(columns=['n_packets', 'total_size', 'base_wait_time', 'n_NACK', 'time_taken', 'drop_rate', 'thruput'])

with open('result.txt', 'r') as fp:
    line = fp.readline()
    ln = 0
    while line:
        if len(line) > 1:
            # print(line)
            # data = [word for word in line.split(' ') if len(word) >= 1 and word[0].isdigit()]
            # print(data)
            # df.loc[ln] = data
            df.loc[ln] = [float(word.strip('.')) for word in line.split(' ') if len(word) >= 1 and word[0].isdigit()]
        line = fp.readline()
        ln += 1
# print(df.iloc[6:12])
print(df.columns)
print(df.head())

# print(df.loc[df['drop_rate'] == 0.1])

p1 = px.box(data_frame=df.loc[df['drop_rate'] == 0.1],
            x='n_packets', y='thruput', color="base_wait_time",
            title='n_packets vs thruput when drop_rate==0.1')
p1.show()

p3 = px.box(data_frame=df.loc[df['n_packets'] == 1000],
            x='base_wait_time', y='thruput', color="drop_rate",
            title='base_wait_time vs thruput when n_packets == 1000')
p3.show()

p2 = px.box(data_frame=df, x='base_wait_time', y='thruput', color="n_packets",
            title='base_wait_time vs thruput')
p2.show()

p01 = px.box(data_frame=df.loc[df['drop_rate'] == 0.1],
             x='n_packets', y='n_NACK', color="base_wait_time",
             title='#packets(Y) vs #retry(n_NACK) when drop_rate==0.1%')
p01.show()

p001 = px.box(data_frame=df.loc[df['drop_rate'] == 1],
              x='n_packets', y='n_NACK', color="base_wait_time",
              title='#packets(Y) vs #retry(n_NACK) when drop_rate==0.1%')
p001.show()

p4 = px.scatter(df.loc[(df['n_packets'] == 1000)], 'n_NACK', 'thruput', title='n_NACK v thruput')
p4.show()

print('maximum thruput is :  ' + str(df['thruput'].max()))

fp.close()
