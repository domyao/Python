


def foot_traffic_main(filename):

    data = data_analyzor(load_data(filename))

    for room_info in data:
        print("Room {}, {} minute average visit, {} visitor(s) total".format(room_info[0], room_info[1][1], room_info[1][0]))



def load_data(filename):

    """
    Import all the data into a dictionary as:

    { <room number> : { <visitor1> : staying time,
                        <visitor2> : staying time,
                        ...
                        }
      <room number> : { <visitor1> : staying time,
                        <visitor2> : staying time,
                        ...
                        }
      ...
    }

    staying time calculated along the way while reading the data



    # frist thought:
    # To read the real "raw data", store both the in and out time in a list
    #
    # if sep[1] not in raw_data:
    #     raw_data[sep[1]] = c.defaultdict(list)
    #
    # raw_data[sep[1]][sep[0]].append(sep[3])
    #
    # second thouht:
    # It may be more convinient to just calculate the staying time of the visitor while reading the file

    """

    raw_data = {}

    with open(filename) as nf:
        for line in nf:
            sep = line.split()      # sep would be like [ <visitor id>, <room num>, <I/O>, <I/O time>]

            if sep[1] not in raw_data:     # if there is no data about the room in raw data
                raw_data[sep[1]] = {}      # then creat a key of the room and assign its value pair to a dict to store its futher visiting info

            if sep[0] not in raw_data[sep[1]]:           # if there is no data about the visitor of this room
                raw_data[sep[1]][sep[0]] = int(sep[3])   # then creat a key of the a visitor,  store the time_stamp as its value pair, the time_stamp must be the in time,
            else:                                        # if there is, then the time_stamp stored last time is the in time, this time is the out time
                raw_data[sep[1]][sep[0]] = int(sep[3]) - raw_data[sep[1]][sep[0]]    # then minus the last store one, get the staying time.

    return raw_data




def data_analyzor(data):

    """
    Futher update the data as:

    { <room number> : [visitors, average time],
      <room number> : [visitors, average time]
      ...
    }

    Then sort it by the room number

    """

    for room, visits in data.items():
        count = len(visits)
        data[room] = [ count, sum(visits.values()) // count]

    return sorted(data.items(), key = lambda item: eval(item[0]))
