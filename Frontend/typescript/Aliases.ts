{
	type NumberOrString = number | string;
	type Timestamp = {nDay: number, nMonth: number, nYear: number} 
	type Bus = {line: NumberOrString, uuid: string, serial: string, timestamp: Timestamp};

	const _getWeekDay = (timestamp: {nDay: number, nMonth: number, nYear: number}): void => {
		console.log(`${timestamp.nDay}/${timestamp.nMonth}/${timestamp.nYear}`)
	}
	const getWeekDay = (timestamp: Timestamp): void => {
		console.log(`${timestamp.nDay}/${timestamp.nMonth}/${timestamp.nYear}`)
	}

	const _getBus = (bus: {line: number | string, uuid: string, serial: string, timestamp: {nDay: number, nMonth: number, nYear: number}}) => {
		console.log(`${bus.line} @ ${bus.uuid}`)
	}
	const getBus = (bus: Bus): void => {
		console.log(`${bus.line} @ ${bus.uuid}`)
	}
}