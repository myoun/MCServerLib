from requests import get
import Prop


class Setup:

    def __init__(self, version: str, xmx: str, xms: str, properties: Properties):
        self.version = version
        self.dowload_url = f"https://papermc.io/api/v1/paper/{self.version}/latest/download"
        self.xmx = xmx
        self.xms = xms
        self.jarname = f"paper-{self.version}.jar"
        self.properties = properties

    def downloadAll(self):

        self.downloadPaper()
        self.makeBatch()
        self.makeEula()

        if self.properties.default != True:
            with open("server.properties", "w") as f:
                ppt_str = ""
                for ppt in self.properties.properties.keys():
                    ppt_str += f"{ppt}={self.properties.properties[ppt]}\n"
                f.write(ppt_str)

    def downloadPaper(self):
        with open(self.jarname, "wb") as f:
            print("페이퍼 버킷을 다운로드 중입니다...\n조금만 기다려 주세요.")
            response = get(self.dowload_url)
            f.write(response.content)
            print("다운로드가 끝났습니다.")

    def makeBatch(self):
        with open("server.bat", "w") as f:
            print("배치파일을 작성중입니다.")
            f.write(
                f"java -Xmx{self.xmx} -Xms{self.xms} -jar {self.jarname} nogui")
            print("배치파일 작성이 끝났습니다.")

    def makeEula(self, boolean=True):
        with open("eula.txt", "w") as f:
            print("Eula 파일을 작성중입니다.")
            f.write("eula=true" if boolean else "eula=false")
            print("Eula 파일 작성이 끝났습니다.")
