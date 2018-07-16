import gzip
import io
import glob
from concurrent import futures
from concurrent.futures import ProcessPoolExecutor


def find_robots(filename):
    robots = set()
    with gzip.open(filename) as  f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

# def find_all_robots(logdir):
#     files = glob.glob(logdir +'/*.log.gz')
#     all_robots = set()
#     for robots in map(find_robots,files):
#         all_robots.update(robots)
#     return all_robots
#
# def find_all_robots(logdir):
#     file = glob.glob(logdir+'/*.log.gz')
#     all_robots = set()
#     with futures.ProcessPoolExecutor() as pool:
#         for robots in pool.map(find_robots,file):
#             all_robots.update(robots)
#     return all_robots
#
#
#
# if __name__ == '__main__':
#     robots = find_all_robots(
#         'logs'
#     )
#     for ipaddr in  robots:
#         print(ipaddr)

def work(x):
    return x
data = [1,2,3,4]
result = map(work,data)
with ProcessPoolExecutor() as pool:
    results = pool.map(work,data)
print(results)