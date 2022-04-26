if __name__ == "__main__":
        try:
                __import__("_____key____").get_token()
        except Exception as e:
                exit(str(e))
