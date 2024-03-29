import socket
import re

data_lst = ['1-FAKE1', '1-FAKE10', '1-FAKE100', '1-FAKE101', '1-FAKE102', '1-FAKE103', '1-FAKE104', '1-FAKE105', '1-FAKE106',
 '1-FAKE107', '1-FAKE108', '1-FAKE109', '1-FAKE10A', '1-FAKE10B', '1-FAKE10C', '1-FAKE10D', '1-FAKE10E', '1-FAKE10F',
 '1-FAKE11', '1-FAKE110', '1-FAKE111', '1-FAKE112', '1-FAKE113', '1-FAKE114', '1-FAKE115', '1-FAKE116', '1-FAKE117',
 '1-FAKE118', '1-FAKE119', '1-FAKE11A', '1-FAKE11B', '1-FAKE11C', '1-FAKE11D', '1-FAKE11E', '1-FAKE11F', '1-FAKE12',
 '1-FAKE120', '1-FAKE121', '1-FAKE122', '1-FAKE123', '1-FAKE124', '1-FAKE125', '1-FAKE126', '1-FAKE127', '1-FAKE128',
 '1-FAKE129', '1-FAKE12A', '1-FAKE12B', '1-FAKE12C', '1-FAKE12D', '1-FAKE12E', '1-FAKE12F', '1-FAKE13', '1-FAKE130',
 '1-FAKE131', '1-FAKE132', '1-FAKE133', '1-FAKE134', '1-FAKE135', '1-FAKE136', '1-FAKE137', '1-FAKE138', '1-FAKE139',
 '1-FAKE13A', '1-FAKE13B', '1-FAKE13C', '1-FAKE13D', '1-FAKE13E', '1-FAKE13F', '1-FAKE14', '1-FAKE140', '1-FAKE141',
 '1-FAKE142', '1-FAKE143', '1-FAKE144', '1-FAKE145', '1-FAKE146', '1-FAKE147', '1-FAKE148', '1-FAKE149', '1-FAKE14A',
 '1-FAKE14B', '1-FAKE14C', '1-FAKE14D', '1-FAKE14E', '1-FAKE14F', '1-FAKE15', '1-FAKE150', '1-FAKE151', '1-FAKE152',
 '1-FAKE153', '1-FAKE154', '1-FAKE155', '1-FAKE156', '1-FAKE157', '1-FAKE158', '1-FAKE159', '1-FAKE15A', '1-FAKE15B',
 '1-FAKE15C', '1-FAKE15D', '1-FAKE15E', '1-FAKE15F', '1-FAKE16', '1-FAKE160', '1-FAKE161', '1-FAKE162', '1-FAKE163',
 '1-FAKE164', '1-FAKE165', '1-FAKE166', '1-FAKE167', '1-FAKE168', '1-FAKE169', '1-FAKE16A', '1-FAKE16B', '1-FAKE16C',
 '1-FAKE16D', '1-FAKE16E', '1-FAKE16F', '1-FAKE17', '1-FAKE170', '1-FAKE171', '1-FAKE172', '1-FAKE173', '1-FAKE174',
 '1-FAKE175', '1-FAKE176', '1-FAKE177', '1-FAKE178', '1-FAKE179', '1-FAKE17A', '1-FAKE17B', '1-FAKE17C', '1-FAKE17D',
 '1-FAKE17E', '1-FAKE17F', '1-FAKE18', '1-FAKE180', '1-FAKE181', '1-FAKE182', '1-FAKE183', '1-FAKE184', '1-FAKE185',
 '1-FAKE186', '1-FAKE187', '1-FAKE188', '1-FAKE189', '1-FAKE18A', '1-FAKE18B', '1-FAKE18C', '1-FAKE18D', '1-FAKE18E',
 '1-FAKE18F', '1-FAKE19', '1-FAKE190', '1-FAKE191', '1-FAKE192', '1-FAKE193', '1-FAKE194', '1-FAKE195', '1-FAKE196',
 '1-FAKE197', '1-FAKE198', '1-FAKE199', '1-FAKE19A', '1-FAKE19B', '1-FAKE19C', '1-FAKE19D', '1-FAKE19E', '1-FAKE19F',
 '1-FAKE1A', '1-FAKE1A0', '1-FAKE1A1', '1-FAKE1A2', '1-FAKE1A3', '1-FAKE1A4', '1-FAKE1A5', '1-FAKE1A6', '1-FAKE1A7',
 '1-FAKE1A8', '1-FAKE1A9', '1-FAKE1AA', '1-FAKE1AB', '1-FAKE1AC', '1-FAKE1AD', '1-FAKE1AE', '1-FAKE1AF', '1-FAKE1B',
 '1-FAKE1B0', '1-FAKE1B1', '1-FAKE1B2', '1-FAKE1B3', '1-FAKE1B4', '1-FAKE1B5', '1-FAKE1B6', '1-FAKE1B7', '1-FAKE1B8',
 '1-FAKE1B9', '1-FAKE1BA', '1-FAKE1BB', '1-FAKE1BC', '1-FAKE1BD', '1-FAKE1BE', '1-FAKE1BF', '1-FAKE1C', '1-FAKE1C0',
 '1-FAKE1C1', '1-FAKE1C2', '1-FAKE1C3', '1-FAKE1C4', '1-FAKE1C5', '1-FAKE1C6', '1-FAKE1C7', '1-FAKE1C8', '1-FAKE1C9',
 '1-FAKE1CA', '1-FAKE1CB', '1-FAKE1CC', '1-FAKE1CD', '1-FAKE1CE', '1-FAKE1CF', '1-FAKE1D', '1-FAKE1D0', '1-FAKE1D1',
 '1-FAKE1D2', '1-FAKE1D3', '1-FAKE1D4', '1-FAKE1D5', '1-FAKE1D6', '1-FAKE1D7', '1-FAKE1D8', '1-FAKE1D9', '1-FAKE1DA',
 '1-FAKE1DB', '1-FAKE1DC', '1-FAKE1DD', '1-FAKE1DE', '1-FAKE1DF', '1-FAKE1E', '1-FAKE1E0', '1-FAKE1E1', '1-FAKE1E2',
 '1-FAKE1E3', '1-FAKE1E4', '1-FAKE1E5', '1-FAKE1E6', '1-FAKE1E7', '1-FAKE1E8', '1-FAKE1E9', '1-FAKE1EA', '1-FAKE1EB',
 '1-FAKE1EC', '1-FAKE1ED', '1-FAKE1EE', '1-FAKE1EF', '1-FAKE1F', '1-FAKE1F0', '1-FAKE1F1', '1-FAKE1F2', '1-FAKE1F3',
 '1-FAKE1F4', '1-FAKE1F5', '1-FAKE1F6', '1-FAKE1F7', '1-FAKE1F8', '1-FAKE1F9', '1-FAKE1FA', '1-FAKE1FB', '1-FAKE1FC',
 '1-FAKE1FD', '1-FAKE1FE', '1-FAKE1FF', '1-FAKE2', '1-FAKE20', '1-FAKE200', '1-FAKE201', '1-FAKE202', '1-FAKE203',
 '1-FAKE204', '1-FAKE205', '1-FAKE206', '1-FAKE207', '1-FAKE208', '1-FAKE209', '1-FAKE20A', '1-FAKE20B', '1-FAKE20C',
 '1-FAKE20D', '1-FAKE20E', '1-FAKE20F', '1-FAKE21', '1-FAKE210', '1-FAKE211', '1-FAKE212', '1-FAKE213', '1-FAKE214',
 '1-FAKE215', '1-FAKE216', '1-FAKE217', '1-FAKE218', '1-FAKE219', '1-FAKE21A', '1-FAKE21B', '1-FAKE21C', '1-FAKE21D',
 '1-FAKE21E', '1-FAKE21F', '1-FAKE22', '1-FAKE220', '1-FAKE221', '1-FAKE222', '1-FAKE223', '1-FAKE224', '1-FAKE225',
 '1-FAKE226', '1-FAKE227', '1-FAKE228', '1-FAKE229', '1-FAKE22A', '1-FAKE22B', '1-FAKE22C', '1-FAKE22D', '1-FAKE22E',
 '1-FAKE22F', '1-FAKE23', '1-FAKE230', '1-FAKE231', '1-FAKE232', '1-FAKE233', '1-FAKE234', '1-FAKE235', '1-FAKE236',
 '1-FAKE237', '1-FAKE238', '1-FAKE239', '1-FAKE23A', '1-FAKE23B', '1-FAKE23C', '1-FAKE23D', '1-FAKE23E', '1-FAKE23F',
 '1-FAKE24', '1-FAKE240', '1-FAKE241', '1-FAKE242', '1-FAKE243', '1-FAKE244', '1-FAKE245', '1-FAKE246', '1-FAKE247',
 '1-FAKE248', '1-FAKE249', '1-FAKE24A', '1-FAKE24B', '1-FAKE24C', '1-FAKE24D', '1-FAKE24E', '1-FAKE24F', '1-FAKE25',
 '1-FAKE250', '1-FAKE251', '1-FAKE252', '1-FAKE253', '1-FAKE254', '1-FAKE255', '1-FAKE256', '1-FAKE257', '1-FAKE258',
 '1-FAKE259', '1-FAKE25A', '1-FAKE25B', '1-FAKE25C', '1-FAKE25D', '1-FAKE25E', '1-FAKE25F', '1-FAKE26', '1-FAKE260',
 '1-FAKE261', '1-FAKE262', '1-FAKE263', '1-FAKE264', '1-FAKE265', '1-FAKE266', '1-FAKE267', '1-FAKE268', '1-FAKE269',
 '1-FAKE26A', '1-FAKE26B', '1-FAKE26C', '1-FAKE26D', '1-FAKE26E', '1-FAKE26F', '1-FAKE27', '1-FAKE270', '1-FAKE271',
 '1-FAKE272', '1-FAKE273', '1-FAKE274', '1-FAKE275', '1-FAKE276', '1-FAKE277', '1-FAKE278', '1-FAKE279', '1-FAKE27A',
 '1-FAKE27B', '1-FAKE27C', '1-FAKE27D', '1-FAKE27E', '1-FAKE27F', '1-FAKE28', '1-FAKE280', '1-FAKE281', '1-FAKE282',
 '1-FAKE283', '1-FAKE284', '1-FAKE285', '1-FAKE286', '1-FAKE287', '1-FAKE288', '1-FAKE289', '1-FAKE28A', '1-FAKE28B',
 '1-FAKE28C', '1-FAKE28D', '1-FAKE28E', '1-FAKE28F', '1-FAKE29', '1-FAKE290', '1-FAKE291', '1-FAKE292', '1-FAKE293',
 '1-FAKE294', '1-FAKE295', '1-FAKE296', '1-FAKE297', '1-FAKE298', '1-FAKE299', '1-FAKE29A', '1-FAKE29B', '1-FAKE29C',
 '1-FAKE29D', '1-FAKE29E', '1-FAKE29F', '1-FAKE2A', '1-FAKE2A0', '1-FAKE2A1', '1-FAKE2A2', '1-FAKE2A3', '1-FAKE2A4',
 '1-FAKE2A5', '1-FAKE2A6', '1-FAKE2A7', '1-FAKE2A8', '1-FAKE2A9', '1-FAKE2AA', '1-FAKE2AB', '1-FAKE2AC', '1-FAKE2AD',
 '1-FAKE2AE', '1-FAKE2AF', '1-FAKE2B', '1-FAKE2B0', '1-FAKE2B1', '1-FAKE2B2', '1-FAKE2B3', '1-FAKE2B4', '1-FAKE2B5',
 '1-FAKE2B6', '1-FAKE2B7', '1-FAKE2B8', '1-FAKE2B9', '1-FAKE2BA', '1-FAKE2BB', '1-FAKE2BC', '1-FAKE2BD', '1-FAKE2BE',
 '1-FAKE2BF', '1-FAKE2C', '1-FAKE2C0', '1-FAKE2C1', '1-FAKE2C2', '1-FAKE2C3', '1-FAKE2C4', '1-FAKE2C5', '1-FAKE2C6',
 '1-FAKE2C7', '1-FAKE2C8', '1-FAKE2C9', '1-FAKE2CA', '1-FAKE2CB', '1-FAKE2CC', '1-FAKE2CD', '1-FAKE2CE', '1-FAKE2CF',
 '1-FAKE2D', '1-FAKE2D0', '1-FAKE2D1', '1-FAKE2D2', '1-FAKE2D3', '1-FAKE2D4', '1-FAKE2D5', '1-FAKE2D6', '1-FAKE2D7',
 '1-FAKE2D8', '1-FAKE2D9', '1-FAKE2DA', '1-FAKE2DB', '1-FAKE2DC', '1-FAKE2DD', '1-FAKE2DE', '1-FAKE2DF', '1-FAKE2E',
 '1-FAKE2E0', '1-FAKE2E1', '1-FAKE2E2', '1-FAKE2E3', '1-FAKE2E4', '1-FAKE2E5', '1-FAKE2E6', '1-FAKE2E7', '1-FAKE2E8',
 '1-FAKE2E9', '1-FAKE2EA', '1-FAKE2EB', '1-FAKE2EC', '1-FAKE2ED', '1-FAKE2EE', '1-FAKE2EF', '1-FAKE2F', '1-FAKE2F0',
 '1-FAKE2F1', '1-FAKE2F2', '1-FAKE2F3', '1-FAKE2F4', '1-FAKE2F5', '1-FAKE2F6', '1-FAKE2F7', '1-FAKE2F8', '1-FAKE2F9',
 '1-FAKE2FA', '1-FAKE2FB', '1-FAKE2FC', '1-FAKE2FD', '1-FAKE2FE', '1-FAKE2FF', '1-FAKE3', '1-FAKE30', '1-FAKE300',
 '1-FAKE301', '1-FAKE302', '1-FAKE303', '1-FAKE304', '1-FAKE305', '1-FAKE306', '1-FAKE307', '1-FAKE308', '1-FAKE309',
 '1-FAKE30A', '1-FAKE30B', '1-FAKE30C', '1-FAKE30D', '1-FAKE30E', '1-FAKE30F', '1-FAKE31', '1-FAKE310', '1-FAKE311',
 '1-FAKE312', '1-FAKE313', '1-FAKE314', '1-FAKE315', '1-FAKE316', '1-FAKE317', '1-FAKE318', '1-FAKE319', '1-FAKE31A',
 '1-FAKE31B', '1-FAKE31C', '1-FAKE31D', '1-FAKE31E', '1-FAKE31F', '1-FAKE32', '1-FAKE320', '1-FAKE321', '1-FAKE322',
 '1-FAKE323', '1-FAKE324', '1-FAKE325', '1-FAKE326', '1-FAKE327', '1-FAKE328', '1-FAKE329', '1-FAKE32A', '1-FAKE32B',
 '1-FAKE32C', '1-FAKE32D', '1-FAKE32E', '1-FAKE32F', '1-FAKE33', '1-FAKE330', '1-FAKE331', '1-FAKE332', '1-FAKE333',
 '1-FAKE334', '1-FAKE335', '1-FAKE336', '1-FAKE337', '1-FAKE338', '1-FAKE339', '1-FAKE33A', '1-FAKE33B', '1-FAKE33C',
 '1-FAKE33D', '1-FAKE33E', '1-FAKE33F', '1-FAKE34', '1-FAKE340', '1-FAKE341', '1-FAKE342', '1-FAKE343', '1-FAKE344',
 '1-FAKE345', '1-FAKE346', '1-FAKE347', '1-FAKE348', '1-FAKE349', '1-FAKE34A', '1-FAKE34B', '1-FAKE34C', '1-FAKE34D',
 '1-FAKE34E', '1-FAKE34F', '1-FAKE35', '1-FAKE350', '1-FAKE351', '1-FAKE352', '1-FAKE353', '1-FAKE354', '1-FAKE355',
 '1-FAKE356', '1-FAKE357', '1-FAKE358', '1-FAKE359', '1-FAKE35A', '1-FAKE35B', '1-FAKE35C', '1-FAKE35D', '1-FAKE35E',
 '1-FAKE35F', '1-FAKE36', '1-FAKE360', '1-FAKE361', '1-FAKE362', '1-FAKE363', '1-FAKE364', '1-FAKE365', '1-FAKE366',
 '1-FAKE367', '1-FAKE368', '1-FAKE369', '1-FAKE36A', '1-FAKE36B', '1-FAKE36C', '1-FAKE36D', '1-FAKE36E', '1-FAKE36F',
 '1-FAKE37', '1-FAKE370', '1-FAKE371', '1-FAKE372', '1-FAKE373', '1-FAKE374', '1-FAKE375', '1-FAKE376', '1-FAKE377',
 '1-FAKE378', '1-FAKE379', '1-FAKE37A', '1-FAKE37B', '1-FAKE37C', '1-FAKE37D', '1-FAKE37E', '1-FAKE37F', '1-FAKE38',
 '1-FAKE380', '1-FAKE381', '1-FAKE382', '1-FAKE383', '1-FAKE384', '1-FAKE385', '1-FAKE386', '1-FAKE387', '1-FAKE388',
 '1-FAKE389', '1-FAKE38A', '1-FAKE38B', '1-FAKE38C', '1-FAKE38D', '1-FAKE38E', '1-FAKE38F', '1-FAKE39', '1-FAKE390',
 '1-FAKE391', '1-FAKE392', '1-FAKE393', '1-FAKE394', '1-FAKE395', '1-FAKE396', '1-FAKE397', '1-FAKE398', '1-FAKE399',
 '1-FAKE39A', '1-FAKE39B', '1-FAKE39C', '1-FAKE39D', '1-FAKE39E', '1-FAKE39F', '1-FAKE3A', '1-FAKE3A0', '1-FAKE3A1',
 '1-FAKE3A2', '1-FAKE3A3', '1-FAKE3A4', '1-FAKE3A5', '1-FAKE3A6', '1-FAKE3A7', '1-FAKE3A8', '1-FAKE3A9', '1-FAKE3AA',
 '1-FAKE3AB', '1-FAKE3AC', '1-FAKE3AD', '1-FAKE3AE', '1-FAKE3AF', '1-FAKE3B', '1-FAKE3B0', '1-FAKE3B1', '1-FAKE3B2',
 '1-FAKE3B3', '1-FAKE3B4', '1-FAKE3B5', '1-FAKE3B6', '1-FAKE3B7', '1-FAKE3B8', '1-FAKE3B9', '1-FAKE3BA', '1-FAKE3BB',
 '1-FAKE3BC', '1-FAKE3BD', '1-FAKE3BE', '1-FAKE3BF', '1-FAKE3C', '1-FAKE3C0', '1-FAKE3C1', '1-FAKE3C2', '1-FAKE3C3',
 '1-FAKE3C4', '1-FAKE3C5', '1-FAKE3C6', '1-FAKE3C7', '1-FAKE3C8', '1-FAKE3C9', '1-FAKE3CA', '1-FAKE3CB', '1-FAKE3CC',
 '1-FAKE3CD', '1-FAKE3CE', '1-FAKE3CF', '1-FAKE3D', '1-FAKE3D0', '1-FAKE3D1', '1-FAKE3D2', '1-FAKE3D3', '1-FAKE3D4',
 '1-FAKE3D5', '1-FAKE3D6', '1-FAKE3D7', '1-FAKE3D8', '1-FAKE3D9', '1-FAKE3DA', '1-FAKE3DB', '1-FAKE3DC', '1-FAKE3DD',
 '1-FAKE3DE', '1-FAKE3DF', '1-FAKE3E', '1-FAKE3E0', '1-FAKE3E1', '1-FAKE3E2', '1-FAKE3E3', '1-FAKE3E4', '1-FAKE3E5',
 '1-FAKE3E6', '1-FAKE3E7', '1-FAKE3E8', '1-FAKE3F', '1-FAKE4', '1-FAKE40', '1-FAKE41', '1-FAKE42', '1-FAKE43',
 '1-FAKE44', '1-FAKE45', '1-FAKE46', '1-FAKE47', '1-FAKE48', '1-FAKE49', '1-FAKE4A', '1-FAKE4B', '1-FAKE4C',
 '1-FAKE4D', '1-FAKE4E', '1-FAKE4F', '1-FAKE5', '1-FAKE50', '1-FAKE51', '1-FAKE52', '1-FAKE53', '1-FAKE54', '1-FAKE55',
 '1-FAKE56', '1-FAKE57', '1-FAKE58', '1-FAKE59', '1-FAKE5A', '1-FAKE5B', '1-FAKE5C', '1-FAKE5D', '1-FAKE5E', '1-FAKE5F',
 '1-FAKE6', '1-FAKE60', '1-FAKE61', '1-FAKE62', '1-FAKE63', '1-FAKE64', '1-FAKE65', '1-FAKE66', '1-FAKE67', '1-FAKE68',
 '1-FAKE69', '1-FAKE6A', '1-FAKE6B', '1-FAKE6C', '1-FAKE6D', '1-FAKE6E', '1-FAKE6F', '1-FAKE7', '1-FAKE70', '1-FAKE71',
 '1-FAKE72', '1-FAKE73', '1-FAKE74', '1-FAKE75', '1-FAKE76', '1-FAKE77', '1-FAKE78', '1-FAKE79', '1-FAKE7A', '1-FAKE7B',
 '1-FAKE7C', '1-FAKE7D', '1-FAKE7E', '1-FAKE7F', '1-FAKE8', '1-FAKE80', '1-FAKE81', '1-FAKE82', '1-FAKE83', '1-FAKE84',
 '1-FAKE85', '1-FAKE86', '1-FAKE87', '1-FAKE88', '1-FAKE89', '1-FAKE8A', '1-FAKE8B', '1-FAKE8C', '1-FAKE8D', '1-FAKE8E',
 '1-FAKE8F', '1-FAKE9', '1-FAKE90', '1-FAKE91', '1-FAKE92', '1-FAKE93', '1-FAKE94', '1-FAKE95', '1-FAKE96', '1-FAKE97',
 '1-FAKE98', '1-FAKE99', '1-FAKE9A', '1-FAKE9B', '1-FAKE9C', '1-FAKE9D', '1-FAKE9E', '1-FAKE9F', '1-FAKEA', '1-FAKEA0',
 '1-FAKEA1', '1-FAKEA2', '1-FAKEA3', '1-FAKEA4', '1-FAKEA5', '1-FAKEA6', '1-FAKEA7', '1-FAKEA8', '1-FAKEA9', '1-FAKEAA',
 '1-FAKEAB', '1-FAKEAC', '1-FAKEAD', '1-FAKEAE', '1-FAKEAF', '1-FAKEB', '1-FAKEB0', '1-FAKEB1', '1-FAKEB2', '1-FAKEB3',
 '1-FAKEB4', '1-FAKEB5', '1-FAKEB6', '1-FAKEB7', '1-FAKEB8', '1-FAKEB9', '1-FAKEBA', '1-FAKEBB', '1-FAKEBC', '1-FAKEBD',
 '1-FAKEBE', '1-FAKEBF', '1-FAKEC', '1-FAKEC0', '1-FAKEC1', '1-FAKEC2', '1-FAKEC3', '1-FAKEC4', '1-FAKEC5', '1-FAKEC6',
 '1-FAKEC7', '1-FAKEC8', '1-FAKEC9', '1-FAKECA', '1-FAKECB', '1-FAKECC', '1-FAKECD', '1-FAKECE', '1-FAKECF', '1-FAKED',
 '1-FAKED0', '1-FAKED1', '1-FAKED2', '1-FAKED3', '1-FAKED4', '1-FAKED5', '1-FAKED6', '1-FAKED7', '1-FAKED8', '1-FAKED9',
 '1-FAKEDA', '1-FAKEDB', '1-FAKEDC', '1-FAKEDD', '1-FAKEDE', '1-FAKEDF', '1-FAKEE', '1-FAKEE0', '1-FAKEE1', '1-FAKEE2',
 '1-FAKEE3', '1-FAKEE4', '1-FAKEE5', '1-FAKEE6', '1-FAKEE7', '1-FAKEE8', '1-FAKEE9', '1-FAKEEA', '1-FAKEEB', '1-FAKEEC',
 '1-FAKEED', '1-FAKEEE', '1-FAKEEF', '1-FAKEF', '1-FAKEF0', '1-FAKEF1', '1-FAKEF2', '1-FAKEF3', '1-FAKEF4', '1-FAKEF5',
 '1-FAKEF6', '1-FAKEF7', '1-FAKEF8', '1-FAKEF9', '1-FAKEFA', '1-FAKEFB', '1-FAKEFC', '1-FAKEFD', '1-FAKEFE', '1-FAKEFF']

word = r'give_div_id'

def main():
    """
    Сервер принимает запросы от клиента и производит вычисление простых математических действий
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", 9910))
        sock.listen(2)
        while True:
            conn_user, addr = sock.accept()
            print(addr)
            with conn_user:
                try:
                    data = conn_user.recv(2048)
                    print(data.decode("utf-8"))
                    div_id = re.findall(word, data.decode("utf-8"))
                    print(div_id)
                    if "give_div_id" in data.decode("utf-8"):
                        print('Ok')
                        conn_user.send(f'HTTP/1.1 200 OK\nServer: localhost:{addr[-1]}\n\n{data_lst[1]}'.encode('utf-8'))
                        print(len(data_lst))
                    elif data == "take".encode("utf-8"):
                        data_lst.append(data.decode("utf-8"))
                        conn_user.send('Ok'.encode("utf-8"))
                        print(data_lst)
                        print(len(data_lst))
                except socket.error:
                    print("Connect not installed...")


if __name__ == "__main__":
    main()
