class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'Profuse stringy salivation' : ['Foot and Mouth Disease'],
            'Vesicular lesions in mouth(palate gums and tongue)' : ['Foot and Mouth Disease'],
            'Pyrexia' : ['Foot and Mouth Disease', 'PPR', 'Babesiosis', 'Thelieriois', 'Trypanosomiasis', 'Anaplasmosis'],
            'Corona of feet and interdigital space' : ['Foot and Mouth Disease'],
            'Sudden death in young calves' : ['Foot and Mouth Disease'],
            'Anorexia' : ['Foot and Mouth Disease', 'Bovine ephemeral fever'],
            'Sudden death' : ['Hog Cholera(Classical swine fever)', 'Enterotaxaemia(by Clostridium Type B C and E)', 'Lead poisoning', 'Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)','Anthrax', 'Organophosphate poisoning'],
            'Fever' : ['Hog Cholera(Classical swine fever)', 'Bluetongue','IBR(Infectious bovine rhinotracheitis)', 'Leptospirosis','Pseudorabies','Foot and Mouth Disease','PPR'], 
            'Purplish colour of skin' : ['Hog Cholera(Classical swine fever)'],
            'Ocular discharge' : ['Hog Cholera(Classical swine fever)',  'IBR(Infectious bovine rhinotracheitis)'],
            'Nervous sign' : ['Hog Cholera(Classical swine fever)','Trypanosomiasis','Arsenic poisoning', 'Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)'],
            'Sudden high fever which subsides after 2-3 days' : ['Bovine ephemeral fever'],
            'Nasal and ocular discharges' : ['Bovine ephemeral fever'],
            'All four feet brought under the body' : ['Bovine ephemeral fever'],
            'Oculonasal purulent discharge' : ['PPR'],
            'Necrotic lesion in mouth' : ['PPR'],
            'Diarrhoea' : ['PPR', 'Contagious ecthyma(Sore mouth or Orf)','Anthrax','Salmonellosis','Arsenic poisonng'],
            'Respiratory distress' : ['PPR', 'Bovine Viral Diarrhoea', 'Thelieriois'],
            'Laminitis and coronitis' : ['Bluetongue','Bovine ephemeral fever'],
            'Erosion in buccal mucosae' : ['Bluetongue'],
            'Blue coloration of tongue' : ['Bluetongue'],
            'Edema of lip and salivation' : ['Bluetongue'],
            'Moderate fever' : ['Bovine Viral Diarrhoea'],
            'Erosive lesion in oral cavity' : ['Bovine Viral Diarrhoea'],
            'Profuse watery diarrhoea' : ['Bovine Viral Diarrhoea'],
            'Lesion in interdigital spaces' : ['Bovine Viral Diarrhoea'],
            'Recurrent reproductive failure' : ['PRRS/SIRS'],
            'Bluish discoloration of ears abdomen and vulva(Blue ear disease)' : ['PRRS/SIRS'],
            'Acute respiratory difficulties(Coughing dyspnoea sneezing etc)' : ['PRRS/SIRS'],
            'Redness of nose' : ['IBR(Infectious bovine rhinotracheitis)'],
            'Respiratory distress and abortion' : ['IBR(Infectious bovine rhinotracheitis)'],
            'Corneal edema' : ['IBR(Infectious bovine rhinotracheitis)'],
            'Conjunctivitis' : ['IBR(Infectious bovine rhinotracheitis)'],
            'Calves less than 6 months may show nervous signs(Encephalitis)' : ['IBR(Infectious bovine rhinotracheitis)'],
            'Progressive loss of body weight' : ['Ovine progressive pneumonia(Maedi-Visna)'],
            'Dysponea(Open mouth breathing)' : ['Ovine progressive pneumonia(Maedi-Visna)', 'Actinomycosis(Lumpy Jaw)','Selenium and vitamin E deficiency','HCN poisoning','Nitrate and Nitrite poisoning','Pseudorabies','Tetanus', 'Organophosphate poisoning'],
            'Hard udder but teats are soft with no or little milk(Hard bag like udder)' : ['Ovine progressive pneumonia(Maedi-Visna)','Caprine Arthritis Encephalitis(CAE)'],
            'Arthritis' : ['Ovine progressive pneumonia(Maedi-Visna)'],
            'Bellowing with hypersensitivity' : ['Rabies'],
            'Incoordination and decreased sensation of hind legs' : ['Rabies'],
            'Salivation' : ['Rabies', 'Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)', 'Organophosphate poisoning','Contagious ecthyma(Sore mouth or Orf)'],
            'Paralysis' : ['Rabies'],
            'Death' : ['Rabies'],
            'Nervous signs with paddling of limbs' : ['Pseudorabies'],
            'Lateral deviation of head' : ['Pseudorabies'],
            'Circling' : ['Pseudorabies','Caprine Arthritis Encephalitis(CAE)','Trypanosomiasis', 'Aflatoxicosis','Listeriosis','Thiamine deficiency'],
            'Continuous bellowing' : ['Pseudorabies'],
            'Excitement in cattle sheep and goat' : ['Pseudorabies'],
            'Intense local pruritis with itching and rubbing' : ['Pseudorabies'],
            'Arthritis(Carpal joint-Big knee)' : ['Caprine Arthritis Encephalitis(CAE)'],
            'Mastitis' : ['Caprine Arthritis Encephalitis(CAE)', 'Listeriosis','Tuberculosis'],
            'Chronic pneumonia' : ['Caprine Arthritis Encephalitis(CAE)'],
            'Unilateral or bilateral posterior paralysis in 1-5 month old kids' : ['Caprine Arthritis Encephalitis(CAE)'],
            'Head tilt' : ['Caprine Arthritis Encephalitis(CAE)'],
            'Torticollis(Turning of head to one side)' : ['Caprine Arthritis Encephalitis(CAE)'],
            'Pustule and sacbs at mouth skin including lips' : ['Contagious ecthyma(Sore mouth or Orf)'],
            'Pain on touch' : ['Contagious ecthyma(Sore mouth or Orf)'],
            'Inappetance' : ['Contagious ecthyma(Sore mouth or Orf)'],
            'Pneumonia' : ['Contagious ecthyma(Sore mouth or Orf)'], 
            'Unilateral facial paralysis(Drooping of ears & paralysis of lips to one side) and dropped jaw' : ['Listeriosis'],
            'Abortion usually in the last trimester of pregnancy' : ['Listeriosis'],
            'Corneal opacity' : ['Listeriosis'],
            'Discharge of blood from nose mouth anus vulva' : ['Anthrax'],
            'Oedematous swelling of face and throat especially in pigs' : ['Anthrax'],
            'Abortion in pregnant' : ['Anthrax'],
            'Generalized muscular rigidity(Sawhorse posture)' : ['Tetanus'],
            'Hyperaesthesia(Extreme alertness)' : ['Tetanus','Lead poisoning','Hypomagnesaemia(Lactation or Grass tenany)'],
            'Prolapse of 3rd eyelid' : ['Tetanus'],
            'Trismus(Jaw muscle stiffening so that it remains tightly closed)' : ['Tetanus'],
            'Respiratory difficulty due to spasm of respiratory muscle' : ['Tetanus'],
            'Progressive symmetrical muscular paralysis(limb jaw and throat muscles affected)' : ['Botulism'],
            'Mydriasis(Dilation of pupil especially in horse)' : ['Botulism'],
            'Tongue paralysis(Hanging out of mouth)' : ['Botulism'],
            'Head tilted to one side or held up or down while walking(Limber neck)' : ['Botulism'],
            'History of recent wound or trauma' : ['Botulism'],
            'Lamb & kid stop milk sucking' : ['Enterotoxaemia(by Clostridium Type B C and E)'],
            'Abdominal pain with bleating' : ['Enterotoxaemia(by Clostridium Type B C and E)'],
            'Diarrhoea sometimes mixed with blood' : ['Enterotoxaemia(by Clostridium Type B C and E)'],
            'Toxaemia' : ['Enterotoxaemia(by Clostridium Type B C and E)'],
            'Cold skin' : ['Colibacillosis'],
            'Pale cool and dry mucosae' : ['Colibacillosis'],
            'Passing of pale yellow to white pasty or watery foul-smelling diarrhoea' : ['Colibacillosis'],
            'Tail and perineum soiled with feces' : ['Colibacillosis'],
            'Mostly seen in 3-5 day old animals' : ['Colibacillosis'],
            'Fibrin in feces' : ['Salmonellosis'],
            'Severe dehydration' : ['Salmonellosis'],
            'Abortion' : ['Salmonellosis','Bovine Viral Diarrhoea'],
            'Gangrene of extremities and arthritis' : ['Salmonellosis'],
            'Sudden high fever' : ['Hemorrhagic septicemia'],
            'Profuse salivation' : ['Hemorrhagic septicemia'],
            'Congested conjunctival mucosa' : ['Hemorrhagic septicemia'],
            'Localization of fluid in throat dewlap brisket' : ['Hemorrhagic septicemia'],
            'Severe dyspnoea' : ['Hemorrhagic septicemia'],
            'Abortion in heifers in the last 3 months of pregnancy however in subsequent pregnancies no abortion' : ['Brucellosis'],
            'Swollen scrotum in bull' : ['Brucellosis'],
            'Swelling of joints(Hygroma)' : ['Brucellosis'],
            'Enlargement of neck & withers(Fistulous withers)' : ['Brucellosis'],
            'Retention of placenta and undulating fever' : ['Brucellosis'],
            'Progressive weakness' : ['Tuberculosis'],
            'Capricious appetite(unpredictable appetite)' : ['Tuberculosis'],
            'Fluctuating temperature' : ['Tuberculosis'],
            'Noisy breathing' : ['Tuberculosis'],
            'Reproductive disorder' : ['Tuberculosis'],
            'Gradual loss of body weight but normal appetite' : ['Paratuberculosis(JD)'],
            'Pea soup-like diarrhoea but absence of foul-smelling epithelial cells mucus(Water hose or pipedream-like diarrhoea terminally)' : ['Paratuberculosis(JD)'],
            'Shedding of wool and weakness in sheep' : ['Paratuberculosis(JD)'],
            'Depression and dyspnoea more seen in goats than sheep' : ['Paratuberculosis(JD)'],
            'Drop in milk yield' : ['Paratuberculosis(JD)','Bovine ephemeral fever'],
            'Initially painless swelling of mandible or maxilla(Jaw) at the level of central molar tooth later painful' : ['Actinomycosis(Lumpy Jaw)'],
            'Swelling of intermandibular space' : ['Actinomycosis(Lumpy Jaw)'],
            'Discharge of sticky honey-like pus' : ['Actinomycosis(LumpyJaw)'],
            'Periodic diarrhea and bloat' : ['Actinomycosis(Lumpy Jaw)'],
            'Excessive salivation' : ['Actinobacillosis(Wooden tongue)'],
            'Swollen and hard tongue' : ['Actinobacillosis(Wooden tongue)'],
            'Presence of nodules and ulcers on the tongue' : ['Actinobacillosis(Wooden tongue)'],
            'Shrunken and immobile tongue which makes eating difficult' : ['Actinobacillosis(Wooden tongue)'],
            'Swollen submaxillary and parotid lymph nodes' : ['Actinobacillosis(Wooden tongue)'],
            'High fever' : ['Glanders'],
            'Cough & nasal discharge' : ['Glanders'],
            'Ulcers on nasal mucosa lower limb skin and abdomen' : ['Glanders'],
            'Characteristic stellate scar on healing of ulcer' : ['Glanders'],
            'Horse develops chronic form(Pulmonary & Skin) and mules & Donkeys acute form' : ['Glanders'],
            'Hemolytic anemia' : ['Leptospirosis'],
            'Stillbirth and abortion' : ['Leptospirosis','Hog Cholera(Classical swine fever)'],
            'Periodic ophthalmia(Blindness) in horses' : ['Leptospirosis'],
            'Milk drop syndrome' : ['Leptospirosis'],
            'Tick infestation' : ['Babesiosis', 'Thelieriois', 'Anaplasmosis'],
            'Anemia' : ['Babesiosis', 'Thelieriois', 'Trypanosomiasis', 'Anaplasmosis','Copper deficiency','Selenium and vitamin E deficiency'],
            'Bloody urine' : ['Babesiosis'],
            'Presence of parasites in blood smear' : ['Babesiosis'],
            'Enlarged superficial lymph nodes' : ['Thelieriois'],
            'Presence of tabanid fly' : ['Trypanosomiasis'],
            'Jaundice' : ['Anaplasmosis','Post parturient hemoglobunaria'],
            'Older age' : ['Anaplasmosis'],
            'Drastic decrease in milk output' : ['Milk Fever'],
            'Decumbency' : ['Milk Fever'],
            'Scant urination and defecation' : ['Milk Fever'],
            'Dry muzzle & dilated pupil' : ['Milk Fever'],
            'Seen 48 hours to 10 days after calving' : ['Milk Fever'],
            'Staggering & convulsion' : ['Hypomagnesaemia(Lactation or Grass tetany)'],
            'Jaw champing' : ['Hypomagnesaemia(Lactation or Grass tetany)','Lead poisoning'],
            'Retraction of eyelids and twitching of ears' : ['Hypomagnesaemia(Lactation or Grass tetany)'],
            'Loud heart sound' : ['Hypomagnesaemia(Lactation or Grass tetany)'],
            'High fever sometimes' : ['Hypomagnesaemia(Lactation or Grass tetany)'],
            'Frogleg attitude' : ['Downers cow syndrome'],
            'Recumbent since 72 hours' : ['Downers cow syndrome'],
            'Bed sores' : ['Downers cow syndrome'],
            'Previous episode of milk fever' : ['Downers cow syndrome'],
            'Appetite and Thirst normal' : ['Downers cow syndrome'],
            'Gradual decrease in food intake and milk yield' : ['Ketosis/Pregnancy toxaemia'],
            'Rapid body weight reduction' : ['Ketosis/Pregnancy toxaemia'],
            'Nervous symptoms' : ['Ketosis/Pregnancy toxaemia'],
            'Ketonic breath' : ['Ketosis/Pregnancy toxaemia'],
            'Usually occurs in the first month of calving' : ['Ketosis/Pregnancy toxaemia'],
            'Rapid reduction in milk output' : ['Post parturient hemoglobinuria'],
            'Brown color urine' : ['Post parturient hemoglobinuria'],
            'Dehydration and difficult breathing' : ['Post parturient hemoglobinuria'],
            'Pica and tachycardia' : ['Post parturient hemoglobinuria'],
            'Mostly seen 2-4 weeks after calving' : ['Post parturient hemoglobinuria'],
            'Loss of milk yield' : ['Copper deficiency'],
            'Changes in coat color' : ['Copper deficiency'],
            'straightness of wool fiber' : ['Copper deficiency'],
            'Sudden falling and death' : ['Copper deficiency'],
            'Persistent diarrhea with watery yellow-green to black feces' : ['Copper deficiency'],
            'Birth of dead or weak lamb' : ['Copper deficiency'],
            'Incoordination' : ['Copper deficiency','Thiamine deficiency'],
            'Alopecia' : ['Zinc deficiency'],
            'Stiff gait and swelling of coronet' : ['Zinc deficiency'],
            'Wrinkling of skin of legs scrotum neck and head' : ['Zinc deficiency'],
            'Reduced body with gain in pigs' : ['Zinc deficiency'],
            'Symmetrical crusty lesions' : ['Zinc deficiency'],
            'Infertility' : ['Zinc deficiency'], 
            'Cyanosis' : ['Selenium and vitamin E deficiency'],
            'Recumbency followed by immediate death in growing pigs(Mulberry heart disease)' : ['Selenium and vitamin E deficiency'],
            'Vomiting' : ['Selenium and vitamin E deficiency'], 
            'staggering and diarrhea(Hepatosis dietetica)' : ['Selenium and vitamin E deficiency'],
            'Retention of fetal membranes' : ['Selenium and vitamin E deficiency'],
            'Flying scapula(Scapula protrude above vertebral column)' : ['Selenium and vitamin E deficiency'],
            'Reduced reproductive performance' : ['Selenium and vitamin E deficiency'],
            'Night blindness with cloudy cornea in calf' : ['Hypovitaminosis A'],
            'Bran-like scales on skin and cracks in hooves' : ['Hypovitaminosis A'],
            'Abortion and stillbirth' : ['Hypovitaminosis A'],
            'Paralysis(Hindleg followed by forelegs)' : ['Hypovitaminosis A'],
            'Congenital defects such as absence of eye(Anophthalmos)/small eye(Microphthalmos) mainly in pigs' : ['Hypovitaminosis A'],
            'Head pressing' : ['Thiamine deficiency','Lead poisoning'],
            'Crossed foreleg and arching of back' : ['Thiamine deficiency'],
            'Accidental ingestion of bracken fern in starvation' : ['Thiamine deficiency'],
            'Tremors of head & neck' : ['Lead poisoning'],
            'Pupil dilation' : ['Lead poisoning'],
            'Violent attack' : ['Lead poisoning', 'Rabies'],
            'Dehydration' : ['Arsenic poisoning'],
            'Blindness' : ['Arsenic poisoning','Aflatoxicosis'],
            'Vomiting even in cattle' : ['Arsenic poisoning'],
            'Accidental access to arsenical insecticides' : ['Arsenic poisoning'],
            'Excitation' : ['Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)'],
            'Muscle tremors' : ['Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)','Urea poisoning'],
            'Paralysis terminally' : ['Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)'],
            'Grinding of teeth' : ['Organochlorine poisoning(DDT Aldrin Dieldrin Chlordane and Heptachlor)'],
            'Tongue protrusion' : ['Organophosphate poisoning'],
            'Impaired vision' : ['Organophosphate poisoning'],
            'Muscle tremor all over the body' : ['Organophosphate poisoning'],
            'Restlessness' : ['Organophosphate poisoning'],
            'Nasal discharge' : ['Organophosphate poisoning','Pseudorabies','Contagious ecthyma(Sore mouth or Orf)'],
            'Frothing' : ['Urea poisoning'],
            'Violent struggling and bellowing' : ['Urea poisoning'],
            'Hypersensitivity' : ['Urea poisoning'],
            'Bloat' : ['Urea poisoning', 'Organophosphate poisoning'],
            'Immediate death(within 10-15 min) after feeding the foliage' : ['HCN poisoning'], 
            'Tremor and restlessness' : ['HCN poisoning'],
            'Brick red mucosa' : ['HCN poisoning'],
            'Weak and rapid pulse with dilatation of pupil' : ['HCN poisoning'],
            'Terminally cyanosis of mucosae' : ['HCN poisoning'],
            'Brown coloration of mucosae' : ['Nitrate and Nitrite poisoning'],
            'Gasping and rapid rate of respiration' : ['Nitrate and Nitrite poisoning'],
            'Severe cyanosis followed by blanching' : ['Nitrate and Nitrite poisoning'],
            'Rapid small and weak pulse' : ['Nitrate and Nitrite poisoning'],
            'Frequent urination' : ['Nitrate and Nitrite poisoning'],
            'Convulsion terminally' : ['Nitrate and Nitrite poisoning'], 
            'Ear twitching' : ['Aflatoxicosis'],
            'Photosensitization' : ['Aflatoxicosis'],
            'Fetlock knuckling' : ['Aflatoxicosis'],
            'Milk fever' : ['PRRS/SIRS'],
            'Abortion or still birth in mid-late term with autolyzed fetuses' : ['PRRS/SIRS'],
            'Subcutaneous oedema' : ['Trypanosomiasis'],
            'Sudden recumbency with mouth over flank' : ['Trypanosomiasis'],
            'Bradycardia' : ['Thiamine deficiency'],
            'Lacrymation' : ['Organophosphate poisoning']
        }

    def get_diseases_for_symptoms(self, symptoms):
    
        symptom_disease_dict = {}
        for symptom in symptoms:

            symptom_disease_dict[symptom] = set(self.knowledge_base[symptom])
    
        common_diseases = set(symptom_disease_dict[list(symptom_disease_dict.keys())[0]])
    
        for symptom in symptoms:
            if symptom in symptom_disease_dict:
                common_diseases.intersection_update(symptom_disease_dict[symptom])
    
        return list(common_diseases)

class UserInterface:
    @staticmethod
    def get_user_input():
        try:
            symptoms = input("Enter symptoms (comma-separated): ").split(',')
            symptoms = [symptom.strip() for symptom in symptoms]
            return symptoms
        except Exception as e:
            print(f"Error: {e}")
            return []

    @staticmethod
    def display_results(possible_diseases):
        if possible_diseases:
            print(f"Possible diseases: {possible_diseases}")
        else:
            print("No matching diseases found.")

def main():
    expert_system = ExpertSystem()
    user_interface = UserInterface()

    try:

        user_symptoms = user_interface.get_user_input()

        possible_diseases = expert_system.get_diseases_for_symptoms(user_symptoms)

        user_interface.display_results(possible_diseases)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()