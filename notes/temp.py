with open("./wifi.log") as reader, open("./wifi_errors.log", "w") as writer:
    for line in reader:
        if "ERROR" in line:
            writer.write(line[line.rfind("ERROR:"):])
