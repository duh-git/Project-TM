from components import Display


class App():
  def __init__(self) -> None:
    d = Display()
    d.mainloop()


if __name__ == '__main__':
  app = App()
  