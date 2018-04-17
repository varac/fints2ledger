class TRetriever:
    def __init__(self, client, accountnumber):
        self.client = client
        self.accountnumber = accountnumber

    def get_hbci_transactions(self, start_date, end_date):
        accounts = self.client.get_sepa_accounts()

        account = self.__find_matching_account(accounts, self.accountnumber)

        return self.client.get_statement(account, start_date, end_date)

    def __find_matching_account(self, accounts, accountnumber):
        for account in accounts:
            if account.accountnumber == accountnumber:
                return account
        raise StopIteration