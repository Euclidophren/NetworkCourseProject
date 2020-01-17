import xml.etree.ElementTree as et


def parse_sys_info(root):
    system_info = root.find("sys")

    if system_info is None:
        return ''

    sys_data = []

    for info in system_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            sys_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(sys_data)

    return result


def parse_processor_info(root):
    processor_info = root.find("processor/item")

    if processor_info is None:
        return ''

    processor_data = []

    for info in processor_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            processor_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(processor_data)

    return result


def parse_memory_info(root):
    memory_info = root.find("memory/item")

    if memory_info is None:
        return ''

    memory_data = []

    for info in memory_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            memory_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(memory_data)

    return result


def parse_motherboard_info(root):
    motherboard_info = root.find("motherboard/item")

    if motherboard_info is None:
        return ''

    motherboard_data = []

    for info in motherboard_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            motherboard_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(motherboard_data)

    return result


def parse_video_card_info(root):
    video_card_info = root.find("video/item")
    if video_card_info is None:
        return ''

    video_card_data = []

    for info in video_card_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            video_card_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(video_card_data)

    return result


def parse_sound_info(root):
    sound_info = root.find("sound/item")

    if sound_info is None:
        return ''

    sound_data = []

    for info in sound_info:
        print(info.tag, info.text, sep=' : ', end='\n')
        if info.text is not None:
            sound_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(sound_data)

    return result


def parse_ip_info(root):
    ip_info = root.findall("ip")

    if ip_info is None:
        return ''

    ip_data = []

    for item in ip_info:
        for info in item:
            print(item.tag, item.text, sep=' : ', end='\n')
            if info.text is not None:
                ip_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(ip_data)

    return result


def parse_disk_info(root):
    disk_info = root.findall("disk")

    if disk_info is None:
        return ''

    disk_data = []

    for item in disk_info:
        for info in item:
            print(info.tag, info.text, sep=' : ', end='\n')
            if info.text is not None:
                disk_data.append(str(info.tag + ":" + info.text + '\n'))

    result = ''.join(disk_data)

    return result


def parse_client_response(filename):
    tree = et.parse(filename)
    root = tree.getroot()

    sys_data = parse_sys_info(root)
    processor_data = parse_processor_info(root)
    memory_data = parse_memory_info(root)
    motherboard_data = parse_motherboard_info(root)
    sound_data = parse_sound_info(root)
    video_card_data = parse_video_card_info(root)
    network_data = parse_ip_info(root)

    return sys_data, processor_data, memory_data, \
        motherboard_data, sound_data, video_card_data, \
        network_data


