carros = ['HRV', 'Porshe', 'Lambo','Sonata','Range Rover', 'Onix', 'Creta', 'gol','corsa'  ]


itCarros =iter(carros)

while True:
    try:
        print(next(itCarros))
    except StopIteration:
        break
    except Exception:
        print('Houve um Erro')
