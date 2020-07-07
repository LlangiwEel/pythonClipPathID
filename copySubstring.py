
import os
className = "className"
dir = os.getcwd()
dir = dir + "/svgFiles/"
list = os.listdir(dir) # dir is your directory path
number_files = len(list)

for filename in os.listdir(dir):
    if filename.endswith(".svg"):
        f = os.path.join(dir, filename)
        s = open(f ,"r")
        def find_between( s, first, last ):
            try:
                start = s.index( first ) + len( first )
                end = s.index( last, start )
                return s[start:end]
            except ValueError:
                return ""
        fileId = filename.split('.')[0]

        classIDU = find_between(filename, "x", '0')
        classIDL = classIDU.replace(classIDU[0], classIDU[0].lower())
        clipPathString = '<clipPath id="' + fileId + '">\n<path \nd=' + find_between(s.read(), "d=", '/>') + ' \nclass="' + classIDL + '" /></clipPath>\n'
        cpi = open('clipPathIds.txt', 'a') #opens .txt in append mode
        cpi.write(clipPathString) #appends clip path IDs into .txt

        cid = open('clipclass.txt', 'r')
        totalCid = cid.read()
        if (classIDL + ',') in totalCid:
            continue
        else:
            cid = open('clipClass.txt', 'a')
            cid.write('.' + classIDL + ',' + '\n')

        #hxt = open('hextileStrings.txt', 'a')
        #hxt.write('import ' + classIDU + ' from ".tiles/' + classIDU + '.svelte"\n')

        #imgPath = open('imgPath.txt', 'a')
        #imgPath.write('`${prefix}/' + classIDL + '/' + fileId + '.jpg`\n')
        #`${prefix}/hillsCold/hexhillsCold00.jpg`,


        continue
    else:
        continue

#<clipPath id="hexForestPineSnowTransition03">
#<path
#d="M 171.5 101 L 179.5 117 L 181 117.5 Q 178.2 118.3 179 122.5 L 181.5 129 Q 183.8 128.3 183 130.5 L 187 137.5 L 187 141.5 L 186 144 Q 190.1 142.3 189 146.5 L 190 153 L 185 152 L 186.5 156 L 187 154 L 190 154 Q 188.9 156.7 191.5 156 L 194 157 L 194.5 159 L 196 151.5 Q 199.7 149.6 200 144.5 Q 197 143.5 198 138.5 L 206 131.5 L 206 125.5 L 214 108.5 L 216.5 106 Q 218.8 105.3 218 107.5 L 223 114.5 L 221 119.5 L 227 128.5 L 225 132.5 L 230 138.5 Q 225.8 140 227 146 L 233 150.5 L 234 157.5 L 232 162.5 L 237 169.5 L 232 172.5 L 236.5 176 L 241 174.5 L 240 179.5 L 241 179.5 L 242 176 Q 244.7 174.9 244 177.5 L 243 179.5 L 244.5 179 L 246 179.5 L 245.5 181 L 250 184.5 L 249 186.5 L 251 187 L 251.5 190 L 254.5 189 Q 252.9 190.8 256 192.5 L 256 384 L 0 384 L 0 192.5 L 3.5 187 L 8.5 186 Q 11.6 180.6 19.5 180 L 21 180.5 Q 19.5 176.1 22.5 177 L 23.5 176 L 26 177.5 Q 25.3 174.9 28 176 L 28.5 178 L 30 173 L 33.5 175 Q 40 172.4 41 164.5 L 40 162.5 Q 44.4 160.5 45 154.5 L 44 152 L 42 151.5 Q 47.3 149.3 48 142.5 L 47 140.5 L 56 129.5 L 58.5 122 L 60 125.5 L 60 127.5 L 61.5 132 L 63 131.5 L 67 140.5 L 66 143.5 L 71 154.5 L 70.5 156 Q 75.5 156.5 76 152.5 L 76.5 151 L 77.5 153 L 79.5 149 L 80.5 151 L 82.5 146 L 83.5 150 L 85.5 147 L 86.5 149 L 89 148 L 96.5 135 L 101 141 L 106 139 L 107.5 136 L 109 136.5 L 109.5 134 L 110.5 136 L 111.5 133 L 112.5 135 Q 115.6 133.6 115 128.5 L 117.5 126 L 122 125 L 123.5 121 L 127.5 123 L 129 118.5 L 126 119.5 L 128 113.5 L 136.5 102 Q 138.8 101.3 138 103.5 L 141 110.5 L 140 113.5 L 144 117.5 L 144 119.5 Q 141.5 121 145 122.5 L 145 128.5 L 149 133.5 Q 148 138 150.5 139 L 153 137.5 L 153.5 139 Q 158 136.5 157 128.5 L 159.5 126 L 164 122.5 L 163 116.5 L 171.5 101 Z M 190 156 L 190 157 L 190 156 Z M 192 157 L 191 159 L 192 159 L 192 157 Z M 32 174 L 32 175 L 32 174 Z M 243 180 L 243 181 L 243 180 Z "
#class="forestPineSnowTransition" />
#</clipPath>
