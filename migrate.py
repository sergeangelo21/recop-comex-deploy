
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()