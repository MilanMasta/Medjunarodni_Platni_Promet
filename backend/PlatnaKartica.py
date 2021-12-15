class PlatnaKartica:

    def __init__(self, broj, imeKorisnika, datumIsteka, sigurnosniKod):
        self.broj = broj
        self.imeKorisnika = imeKorisnika
        self.datumIsteka = datumIsteka
        self.sigurnosniKod = sigurnosniKod
        self.ukupanIznos = 70

    def get_broj(self):
        return self.broj

    def set_broj(self, broj):
        self.broj = broj

    def get_imeKorisnika(self):
        return self.imeKorisnika

    def set_imeKorisnika(self, imeKorisnika):
        self.imeKorisnika = imeKorisnika

    def get_datumIsteka(self):
        return self.datumIsteka

    def set_datumIsteka(self, datumIsteka):
        self.datumIsteka = datumIsteka

    def get_sigurnosniKod(self):
        return self.sigurnosniKod

    def set_sigurnosniKod(self, sigurnosniKod):
        self.sigurnosniKod = sigurnosniKod

    def get_ukupanIznos(self):
        return self.ukupanIznos

    def set_ukupanIznos(self, ukupanIznos):
        self.ukupanIznos = ukupanIznos
