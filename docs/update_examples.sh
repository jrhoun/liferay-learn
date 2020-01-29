#!/bin/bash

for dir_name in `find commerce/2.x/en/developer-guide/tutorials -maxdepth 2 -name *.zip -type d`
do
	cp -fr commerce/2.x/en/developer-guide/tutorials/_template/* ${dir_name}

	#pushd ${dir_name}

	#./gradlew classes formatSource

	#popd
done

for file_name in `find commerce/2.x/en/developer-guide/tutorial -name gradle-wrapper.properties -type f`
do
	input=$file_name
	echo "$input"
	filepath=${input%%gradle-wrapper.properties}
	while IFS= read -r line
	do
		echo ${line//gradle-4.10.2-bin.zip/gradle-5.5.1-bin.zip} >> $filepath/gradle-wrapper.properties.temp
	done < "$input"
	mv $filepath/gradle-wrapper.properties.temp $filepath/gradle-wrapper.properties
done

