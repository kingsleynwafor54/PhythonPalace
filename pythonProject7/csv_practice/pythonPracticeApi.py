data={
  "coord": {
    "lon": -114.6244,
    "lat": 32.7243
  },
  "list": [
    {
      "radiation": {
        "ghi": 206.68,
        "dni": 2.27,
        "dhi": 204.83,
        "ghi_cs": 826.71,
        "dni_cs": 885.47,
        "dhi_cs": 114.93
      },
      "dt": 1618232400
    }
  ]
}

print(data['list'][0]['dt'])
